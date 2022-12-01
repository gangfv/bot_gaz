from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

gro_text: str = "Газпром газораспределение"
rkg_text: str = "Газпром межрегионгаз"
back_text: str = "Назад"

gro_contract: str = "Действующий договор ТО ВДГО"
gro_planned_date: str = "Планируемая дата ТО ВДГО"
gro_amount_debt: str = "Сумма задолженности за ТО ВДГО"
gro_applic_same: str = "Заявка на ТО ВДГО"
gro_price_list: str = "Прейскурант цен на услуги ГРО"
gro_safety_rules: str = "Правила газовой безопасности"
gro_contact: str = "Контакты"
gro_applic_same: str = "Узнать статус заявки на догазификацию"
gro_inretact_map: str = "Интерактивная карта догазификации"

rkg_amount_debt: str = "Сумма задолженности"
rkg_date_amount: str = "Дата и сумма последней оплаты"
rkg_date_value: str = "Дата и величина (числовое значение) последних показаний счетчика"
rkg_transm_meter_read: str = "Передача показаний счетчика"
rkg_list_doc: str = "Перечень документов для переоформления лицевого счета и для изменения параметров лицевого счета по категориям"
rkg_req_cont_reasons: str = "Заявка на выход контролера по причинам"
rkg_about_proced_gaz: str = "Информирование о порядке возобновления поставки газа по категориям"
rkg_about_term_contr: str = "Информирование о порядке расторжения договора поставки"

gro_bt = KeyboardButton(gro_text)
rkg_bt = KeyboardButton(rkg_text)
back_bt = KeyboardButton(back_text)

mr_start = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).row(
    gro_bt, rkg_bt
)

mr_gro = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).row(
    back_text
)

mr_rkg = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).row(
    back_text
)