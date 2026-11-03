---
content_hash: f242954f5cf8182a77b26c73ba15b896e90a2bc9920b44aff9607c09c512f771
fetched_at: '2026-06-29T00:10:02.606464+00:00'
page_id: '452718976'
product: rm
source: tdn-rm
title: Parâmetros de Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718976
version: 9
---

11Integração Carol/TSA

* **Utilizar integração com o TSA:** Habilitando esse parâmetro será considerado a integração entre TOTVS Automação de Ponto e TOTVS Segurança e Acesso.
* **Importar batidas integradas via API:** Habilitando esse parâmetro será considerada a importação das batidas integradas via API. Esse parâmetro será habilitado sempre que o parâmetro "Utilizar integração com TSA" estiver marcado .
* **Considera integração com as batidas da Carol:** Habilitando este parâmetro, surgirão os campos para parametrização do ambiente, onde deverão ser informadas as credenciais de acesso à integração com a Carol Clock-In.
* **Importa batidas fora do perímetro:** Por default, este campo sempre virá marcado, e ao desmarcá-lo, as batidas fora do perímetro originadas de importação com o Clock-in serão desconsideradas do espelho do funcionário, porém ainda ficarão visíveis para os relatórios ficais, como o AFDT. A justificativa padrão deste processo é "A batida foi realizada fora de perímetro pré-definido para colaborador". Este processo é irreversível, portanto uma vez desmarcado e as batidas importadas, não será possível reconsiderá-las no espelho.
2TOTVS Assinatura Eletrônica

* **Utilizar e-mail pessoal do destinatário caso o principal não esteja preenchido**:

Quando habilitado, ao enviar o Espelho do Cartão de Ponto ou o Espelho do Ponto Digital para assinatura eletrônica, o sistema enviará o arquivo para o e-mail pessoal do funcionário caso o e-mail principal não esteja informado.

Quando desabilitado, o sistema sempre enviará o Espelho do Cartão de Ponto ou o Espelho do Ponto Digital para assinatura eletrônica ao e-mail principal do funcionário.

**Localização dos campos no sistema:**  
**E-mail principal:** *Cadastro de Funcionários > Informações Pessoais > Identificação > E-mail*

**E-mail pessoal:** *Cadastro de Funcionários > Informações Pessoais > Endereço Principal > EMAILPESSOAL*

Versões:

Recurso disponível a partir das versões **12.1.2510.173** e **12.1.2602.100**.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Assistente de Implantação de Processos
