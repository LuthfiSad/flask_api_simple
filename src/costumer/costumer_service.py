from .costumer_repository import CostumerRepository
from ..utils.paginate_data import paginate_data
from ..utils.error_validate import error_validate
from ..utils.messages import MESSAGES
from ..utils.handle_response import handle_response

def validate_costumer_data(name, email, id=None):
    if not name:
        return error_validate(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["REQUIRED"]["NAME"])
    if not email:
        return error_validate(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["REQUIRED"]["EMAIL"])
    exist = CostumerRepository.find_by_email(email)
    if exist and exist.id != id :
        return error_validate(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["ALREADY"]["EMAIL"])
  
def get_all_costumers(page, per_page, search_term):
    # Fetch all costumers from the repository
    costumers = CostumerRepository.find_all()
    
    # Apply search filtering
    if search_term:
        filtered_costumers = [costumer for costumer in costumers if search_term.lower() in costumer.name.lower() or search_term.lower() in costumer.email.lower()]
    else:
        filtered_costumers = costumers

    # Apply pagination
    paginated_costumers, meta = paginate_data(filtered_costumers, page=page, per_page=per_page)

    # Prepare costumer data
    costumer_data = [{'id': costumer.id, 'name': costumer.name, 'email': costumer.email} for costumer in paginated_costumers]

    return handle_response(status=200, code="SUCCESS", message=MESSAGES["SUCCESS"]["COSTUMER"]["GET"], data=costumer_data, meta=meta)

def create_costumer(name, email):
    errors = validate_costumer_data(name, email)
    
    if errors:
      return handle_response(
        status=errors["status"],
        code=errors['code'],
        message=errors['message'],
      )
      
    CostumerRepository.add(name, email)
    return handle_response(status=201, code="SUCCESS",message=MESSAGES["SUCCESS"]["COSTUMER"]["POST"])
    

def update_costumer(costumer_id, name, email):
    costumer = CostumerRepository.find_by_id(costumer_id)
    if not costumer:
      return handle_response(status=400, code="NOT_FOUND", message=MESSAGES["ERROR"]["NOT_FOUND"]["COSTUMER"])
    
    errors = validate_costumer_data(name, email, costumer_id)
    if errors:
      return handle_response(
        status=errors["status"],
        code=errors['code'],
        message=errors['message'],
      )
      
    costumer.name = name
    costumer.email = email
    CostumerRepository.update(costumer)
    return handle_response(status=201, code="SUCCESS",message=MESSAGES["SUCCESS"]["COSTUMER"]["UPDATE"])

def delete_costumer(costumer_id):
    costumer = CostumerRepository.find_by_id(costumer_id)
    if not costumer:
      return handle_response(status=400, code="NOT_FOUND", message=MESSAGES["ERROR"]["NOT_FOUND"]["COSTUMER"])
    CostumerRepository.delete(costumer)
    return handle_response(status=201, code="SUCCESS",message=MESSAGES["SUCCESS"]["COSTUMER"]["DELETE"])
