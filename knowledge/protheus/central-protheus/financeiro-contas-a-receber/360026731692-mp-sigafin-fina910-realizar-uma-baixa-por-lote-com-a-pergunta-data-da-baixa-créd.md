---
article_id: 360026731692
category: Financeiro - Contas a Receber
content_hash: 186c47e1cecb776e6e0e712e84ad9bd60a12e028d452c7e3d753ec3217a1f77b
fetched_at: '2026-06-28T22:38:15.088833+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'MP - SIGAFIN - FINA910- Realizar uma baixa por lote com a pergunta Data da
  Baixa = Crédito SITEF e baixa com a data base '
type: support-article
updated_at: '2021-04-28T15:17:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026731692-MP-SIGAFIN-FINA910-Realizar-uma-baixa-por-lote-com-a-pergunta-Data-da-Baixa-Cr%C3%A9dito-SITEF-e-baixa-com-a-data-base
---

**Ocorrência**Ao realizar uma **baixa por lote** na rotina do **Conciliador TEF** aoselecionar a pergunta **Data da Baixa = Crédito SITEF**,o sistema desconsidera essa pergunta e baixa com a **data base** que o usuário está logado no sistema.

**Ambiente**Microsiga Protheus – Financeiro – FINA910– A partir da versão 11.8

**Causa**Com o parâmetro **MV\_BXCNAB = S**, o sistema está correto pegar a data Base, mesmo inserido a data do Crédito.

**Solução**Com o preenchimento do parâmetro **MV\_BXCNAB = S**considera a data Base, pois existem várias datas dos registros dentro de um lote e o valor será acumulado em uma única data a qual será a data base.  
  
Exemplo: Vamos supor que uma empresa está com o parâmetro **MV\_BXCNAB=S** e recebeu um **arquivo de retorno** do *sotfware* *express* onde tem os seguintes títulos:  
Título A valor R$ 100,00 data do crédito **15/04/2019**  
Título B valor R$ 200,00 data do crédito **22/04/2019**  
Título C valor R$ 300,00 data do crédito **29/04/2019**  
Ao logar no sistema com data do dia **10/04/2019** e utilizar o parâmetro **MV\_BXCNAB=S**, os registros serão baixados sem movimentar **banco** (**E5\_TIPODOC=BA**) e será criado uma linha totalizadora onde essa irá fazer a movimentação bancária no valor aglutinado de R$ 600,00, porém o sistema não irá saber qual a **data de crédito** que será considerada no totalizado. Será com a data 15/04/2019 ou 22/04/2019 ou com a data 29/04/2019?  
  
Então por padrão do sistema a **data do crédito** ao ser usada no totalizador sempre será a data logada do sistema.  
  
**Importante:**  
 Esse procedimento de gravação da data do crédito é válido para o **CNAB**.
