---
article_id: 1500003211561
category: Integrações Nativas
content_hash: ed76476627d45dc9bf83067c8c352f14d0b812d5fdf53593dfbd4eaff75f5f2a
fetched_at: '2026-06-28T22:42:35.425978+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Inclusão de Pneus via Documento de Entrada
type: support-article
updated_at: '2026-03-26T11:24:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003211561-Manufatura-Linha-Protheus-MNT-Inclus%C3%A3o-de-Pneus-via-Documento-de-Entrada
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39282411635607)*** Tempo aproximado para leitura: **00:02:40 min**  
  
**Dúvida**  
Como é realizada a inclusão de **Pneus** via **Documento de Entrada**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Todas as versões  
  
**Solução**  
Para realizar a inclusão de **Pneus** em lote através da rotina de **Documento de Entrada - MATA103**, siga os passos abaixo:

* Acesse o módulo de **Manutenção de Ativos e Gestão de Frotas** **- SIGAMNT** e em **Atualizações / Controle de Oficina / Bens /** [**Status - MNTA710**](https://tdn.totvs.com/pages/viewpage.action?pageId=471953731) e incluir um **Status** para **pneus**;
* Acessar o módulo de **Estoque/Custos - SIGAEST** e em **Atualizações / Cadastro / Produto / Grupos - MATA035**, incluir um grupo para identificar os **pneus** no módulo de **Estoque**;
* Em **Atualizações / Cadastro / Produto / Produtos - MATA010**, incluir um **produto** e preencher o campo **Grupo - B1\_GRUPO** com o **Código do grupo** incluído anteriormente;
* Altere o parâmetro **MV\_NGPNGR - Código do Grupo de Produto do tipo Pneu** informando o **código** **do grupo** de produto que será considerado do tipo **Pneu** no ambiente de **Estoque/Custos**;
* Altere o parâmetro **MV\_NGSTAFG - Código do status que identifica o aguardo da liberação da marcação de número de fogo** informando o **Código padrão** para o **status** dos **Pneus** incluídos pelo módulo de **Estoque/Custos**;
* Altere o parâmetro **MV\_NGMNTES - Integração com estoque** para ativar a integração com o módulo **SIGAEST**, preenchendo o campo com **S - Sim**;
* Acesse o módulo **SIGAEST** em **Atualizações / Movimentações / Fiscais / Documento de Entrada - MATA103**;
* Selecione a opção **Incluir** e o Sistema exibirá a tela para preenchimento dos dados do documento de entrada. Preencher os campos obrigatórios;
* No campo **Produto - D1\_COD** atribuir o **código do produto** cadastrado anteriormente. No campo **Quantidade - D1\_QUANT** informar a quantidade de pneus que serão incluídos. Confira os dados e **confirme**;

Para releases anteriores a 12.1.2310:

* Se não houver bens do tipo **Pneu** cadastrados no Sistema será exibida uma tela para atribuir o primeiro **Código de pneu**. Este será utilizado como base para a geração dos códigos sequenciais.
* Será exibida a tela de **Inclusão de Lote de Pneus**. Preencher os campos de **complemento dos pneus**. Confira os dados e **confirme**;
* Acesse o módulo **SIGAMNT** em **Atualizações / Controle de Pneus / Pneus /** [**Pneus - MNTA083**](https://tdn.totvs.com/pages/viewpage.action?pageId=519197237). Verificar que foram incluídos os bens do tipo **Pneu**;
* Selecionar um pneu e selecionar a opção **Alterar**. Verificar que é possível alterar o campo **Status - T9\_STATUS**do pneu;
* Selecionar a pasta **Pneu**, verificar que é possível alterar o campo **Nº de Fogo Pneu - TQS\_NUMFOG**.

Para releases igual ou superior a 12.1.2310:

* Após a inclusão do documento de entrada será necessário utilizar a rotina **Atualizações / Controle de Pneus / Pneus /** [**Pneus a Partir de NF - MNTA085**](https://tdn.totvs.com/pages/viewpage.action?pageId=655443443) para a inclusão dos pneus que vão aguardar a marcação de fogo / Classificação.
* Após a inclusão dos pneus será necessário realizar o processo de **Atualizações / Controle de Pneus / Pneus /** [**Classificação de Pneus - MNTA086**](https://tdn.totvs.com/pages/viewpage.action?pageId=781846882)

**Importante**  
Se existir no Sistema o cadastro de ao menos um **pneu**, o Sistema gerará os **códigos dos pneus** incluídos em lote sequencialmente com base no **código do pneu** já existente.
