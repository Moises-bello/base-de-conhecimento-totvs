---
content_hash: 660eed2296f60c717d46b34f1c8b01d710bdc27bd8c0973541927b5ce9c9624f
fetched_at: '2026-06-29T00:10:03.694330+00:00'
page_id: '452719131'
product: rm
source: tdn-rm
title: Ocorrências Acidente de Trabalho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719131
version: 5
---

**Ocorrências Acidente de Trabalho**

---

O Cadastro de Ocorrências de Acidente de Trabalho tem como objetivo controlar e acompanhar as ocorrências de acidentes ocorridas na empresa.   
  
**Emitente:** Nesta pasta se encontram os principais dados e informações da ocorrência e do Funcionário acidentado. Nesta pasta é feito o cadastro de novas ocorrências, ou alteração dos dados básicos sobre elas, contendo campos destinados ao preenchimento de dados.   
**Observação:** Quando é feita a inclusão de uma CAT do Tipo "Reabertura", ao informar a CAT de origem o sistema irá retornar o código da CAT de origem e no campo descrição trará as informações constantes no campo "Descrição da situação geradora do acidente ou doença:". Caso esse campo não esteja preenchido, o sistema exibirá somente o código da CAT de origem e a descrição em branco.

**Atenção:**

* A situação geradora foi especificada pelo governo conforme "Manual de Orientação do eSocial" e será informada conforme listagem disponível para seleção.

**Observação:**

No cadastro de Fonte Geradora existe um parâmetro para informar o tipo da fonte geradora, se Agente Causador ou Situação Geradora. Este parâmetro será utilizado para separar onde será listado o item cadastrado.

**Exemplo:**

Fonte Geradora – 200012200 – marcado como *Tipo de*Agente 'Situação Geradora Acidente Trabalho'.  
Fonte Geradora – 302010300 – marcado como *Tipo de*Agente 'Agente Causador Acidente Trabalho'.  
Fonte Geradora – 200004600X – marcado como *Tipo de*Agente 'Agente Causador Doença Profissional'.  
   
Em *CAT | Ocorrências Acidente Trabalho*:  
No campo *Código da situação geradora* será listado apenas o código 200012200.  
No campo *Cód. Agente(s) Causador(es)* será listado os códigos 302010300 e 200004600X.

**Atenção:**

A listagem de Situação geradora e Agente Causador dependerão do cadastro de Fonte Geradora que deverá ter informados obrigatoriamente os campos: Código do ESocial, Tipo de Agente e Ativo.

* Com a definição do eSocial cada cadastro de acidente de trabalho pode haver um ou mais Cód. Agente(s) Causador(es). Este código do agente causador foi especificado pelo governo conforme "Manual de Orientação do eSocial" e deverá conter os valores fixos.
* No eSocial as Parte(s) do corpo atingida(s) no cadastro de acidente de trabalho deverão obedecer o documento "Manual de Orientação do eSocial".
* Como o governo definiu valores fixos para "Partes do corpo atingidas", no cadastro de natureza não serão permitidas edições nem inserções de registro.

**Importante:**

Nesta pasta se encontram os dados que foram criados para adequação à "PORTARIA SEPRT/ME Nº 4.334, DE 15 DE ABRIL DE 2021".  
Para essa adequação foram criados os campos: Fonte do Cadastro, Número da CAT, Data de Recebimento, Número do recibo do evento da CAT de origem e CAT Excluída.

Vale ressaltar que para geração de gatilhos para o eSocial a CAT deve ter a marcação na fonte de cadastro como eSocial e estar com a versão do Layout e Data de Início de SST definidas (estas duas últimas no parametrizador da Folha de Pagamento). Uma vez que a fonte de cadastro for definida como eSocial todos os campos novos ficarão bloqueados e serão atualizados mediante execução de processo.

Quando a fonte de cadastro for CAT Web, os campos Número da CAT e Data de Recebimento serão liberados para que o usuário entre com estes dados.  
O campo CAT Excluída nunca será de ação manual, ou seja, somente via processo é que este poderá ser manipulado.

Foram disponibilizados dois processos no cadastro da CAT

  - Atualiza Dados da CAT eSocial:

Este processo faz a atualização do Número da CAT e da Data de Recebimento, assim como do Número do recibo do evento da CAT de origem em caso de retificação ou exclusão.

  - Gerar Exclusão para eSocial:

Este processo faz uma exclusão virtual, ou seja, não exclui o registro do sistema, mas gera um evento S-3000 para o eSocial. Essa exclusão virtual é necessária, pois, do contrário não seria possível emitir relatório para o acidentado e nem para o sindicato. Entretanto, após confirmação da exclusão da CAT no governo o cadastro da CAT ficará todo desabilitado a fim de que nenhuma informação seja alterada.

Estes processos só podem ser executados em registros cujas fonte de cadastro esteja definida como eSocial.  
Na visão das Ocorrências de Acidente de Trabalho foram disponibilizadas duas colunas para facilitar a identificação da Fonte de Cadastro e se a CAT foi ou se está em processo de exclusão.

**Local do Acidente:**Nesta pasta encontram se os principais dados e informações do local de acidente:

* Local do acidente (INSS)
* Especificação do local do acidente
* Logradouro do local do acidente
* Número do local do acidente
* UF do local do acidente
* Código do município do acidente - informar o município conforme o cadastro do IBGE.
* CNPJ do local do acidente - Deverá ser preenchido quando o acidente ou doença ocupacional ocorrer em empresa onde a empregadora presta serviço.

**Atestado Médico:** Nesta pasta encontram se os principais dados referentes ao atendimento médico, informações médicas e atestado permitindo descrever detalhadamente a ocorrência de acidente de trabalho com as informações do atendimento gerado na ocorrência de acidente de trabalho.

**Atenção:**

* Conforme solicitação do eSocial foi criado o campo Código de atendimento médico(CNES) para armazenar o código da unidade de atendimento médico do cadastro nacional de estabelecimento de saúde.
* Médico – Selecionar do cadastro feito anteriormente no Cadastro de Profissional de Saúde.

**Medidas:** A pasta de Medidas é destinada ao cadastro das medidas que devem ser tomadas para cada tipo de ocorrência.

**Envolvidos:** A pasta é destinada ao cadastro das pessoas envolvidas na ocorrência de acidente de trabalho.

**Fotos:** O Cadastro de Fotos tem como objetivo armazenar as fotos tiradas do local, posto de trabalho, equipamento, etc., que envolveu o acidente de trabalho.

**Campos Complementares:** O cadastro dos campos complementares tem como objetivo, armazenar informações complementares além das quais o aplicativo já disponibiliza nas pastas apresentadas na janela de edição, visando atender às necessidades específicas da empresa em relação às pessoas cadastradas na base, independente de seu status.

**Atenção**

Os campos complementares deverão ter tido seus cadastros previamente efetuados através do menu Cadastros / Campos complementares, nestas pastas citadas acima os mesmos só se encontrarão disponibilizados para visualização e edição de valores.

Para qualquer ícone desabilitado, verifique com o Supervisor as permissões do usuário em questão em Cadastros | Segurança | Perfis | pasta Acesso a Menus.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Investigação Testemunhas de Acidente de Trabalho RNT

|  |  |
| --- | --- |
|  | Como Fazer |

---

Cópia entre Coligadas
