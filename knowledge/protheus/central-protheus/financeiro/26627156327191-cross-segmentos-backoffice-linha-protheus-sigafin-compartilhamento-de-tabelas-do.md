---
article_id: 26627156327191
category: Financeiro
content_hash: bb8bfc9f139506b594f113be8ec71f4fdc98f5410a5a60ec0bbccc391da9f7a3
fetched_at: '2026-06-28T22:38:00.951829+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Compartilhamento de
  tabelas do módulo Financeiro
type: support-article
updated_at: '2024-09-26T20:22:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26627156327191-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Compartilhamento-de-tabelas-do-m%C3%B3dulo-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26628108586391) Tempo aproximado para leitura: **00:10:00****min**

**Dúvida**

Como realizar a validação das tabelas família FKs e evitar inconsistência na gravação dos dados

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Importante**

A estrutura das tabelas deve ser definida durante a implantação do sistema, conforme as necessidades pré-estabelecidas.

**Desaconselhamos a alteração no compartilhamento das tabelas após a implantação do sistema**, pois tal modificação pode comprometer a confiabilidade da base de dados.

**Solução**

Todas as tabelas da família **SE5**, devem ter o mesmo compartilhamento, exceto o **SED e SE8**.

**Tabelas da Família FK (FK0 até FKZ):**

1. **Tabelas da Reestruturação da SE5:** Deve-se utilizar o mesmo compartilhamento da tabela SE5 nas tabelas. **Link Correspondente:** [Reestruturação da tabela SE5 na família de tabelas FKx](https://tdn.totvs.com/pages/releaseview.action?pageId=183730415)
2. **Tabela FK0:** Relaciona-se com o Configurador de Tributos (item abaixo), mas deve ter o mesmo compartilhamento indicado no link acima.
3. **Configurador de Tributos:** As tabelas do Configurador de Tributos (por exemplo, **FKK até FKV**) devem ser definidas com o mesmo compartilhamento. A relação das tabelas pode ser consultada no **Link Correspondente:** [Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/PROT/Configurador+de+Tributos+-+Regras+Financeiras).
4. **Complemento de Título:** As tabelas **FKF e FKG** devem ser definidas com o mesmo compartilhamento dos títulos (**SE1 e SE2**).  Link: [DT Cadastro de Complemento do Título.](https://tdn.totvs.com/pages/viewpage.action?pageId=281128084)
5. **Cadastros "Complemento de Imposto" e "Natureza de Rendimento" (REINF):** As tabelas **FKE**, **FKX e FKZ** são de cadastro e podem ser definidas com o compartilhamento conforme a necessidade.
6. **Vínculo de "Títulos x Naturezas de Rendimento" (REINF):** A tabela **FKW** deve ser definida com o mesmo compartilhamento da tabela **FKF**. A tabela **FKY** deve ter o mesmo compartilhamento da tabela **SE5**.
7. **Rateio de IR Progressivo:** A tabela **FKJ** deve ser mantida com o mesmo status da tabela **SA2**.
8. **Valores Acessórios:** O compartilhamento da tabela **FKD** deve ser definido com o mesmo compartilhamento dos títulos (**SE1 e SE2**). A tabela **FKC** é de cadastro e pode ter o compartilhamento conforme a necessidade.

**Liquidação de Contas a Receber (FINA460)**

O compartilhamento das tabelas **FO0, FO1 e FO2** deve ser igual ao da tabela **SE1**.

**Tabelas de Rastreamento de Contas a Pagar (FI8) e Contas a Receber (FI7)**

O modo de compartilhamento aplicado às tabelas **SE1 e SE2** deve ser obrigatoriamente adotado nas tabelas **FI7 e FI8**, a fim de garantir a manutenção do vínculo.

**Link Correspondente:** [Compartilhamento de tabela para rastreamento financeiro](https://tdn.totvs.com/display/PROT/FIN0064_Compartilhamento_de_tabela_para_rastreamento+financeiro)

**Extrato Bancário e Reprocessamento de Saldos:**

O compartilhamento das tabelas **SA6, SE5 e SE8** impacta diretamente o **reprocessamento de saldos (FINA210)** e a visualização das movimentações no **extrato bancário (FINR470)**.

**Link Correspondente:** [compartilhamento de tabelas de reprocessamento de saldo](https://tdn.totvs.com/pages/viewpage.action?pageId=327323352)

Ou busque no TDN por: Compartilhamento de tabela para reprocessamento de saldo bancário.

Se a tabela **SE5** estiver configurada como Exclusiva, não será possível visualizar os registros de todas as filiais no **Extrato Bancário (FINR470)**. Quando a **SE5** é configurada por **filial (exclusiva)**, a visualização das movimentações ficará restrita à filial em que o usuário está logado.

**Link Correspondente:** [FINR470 - SA6 compartilhada](https://tdn.totvs.com/display/PROT/TUUOUD_DT_FINR470_SA6_COMPARTILHADA)

Entretanto, caso o cliente necessite gerar realmente os dados de todas as filiais, isso pode ser feito através do ponto de entrada **F470ALLF**.

**Link Correspondente:** [F470ALLF - Sinalização para tratamento do extrato](https://tdn.totvs.com.br/pages/releaseview.action?pageId=6071573)

**Refaz Cli/For (FINA410):**

Para o compartilhamento das tabelas, não é permitido ter cadastros (**SA1/SA2**) configurados como exclusivos e movimentos compartilhados (**SE1/SE2/SE5**).

**Link Correspondente:** [Compartilhamento de tabelas de cadastro x movimento](https://tdn.totvs.com/pages/viewpage.action?pageId=844959467)

**Cálculo/Recalculo de Comissões (FINA440):**

Para o compartilhamento das tabelas, não é permitido ter cadastros (**SA3**) configurados como exclusivos e movimentos compartilhados (**SE3**).

**Link Correspondente:**

* **FAT0307**: [Compartilhamento de tabelas relacionadas ao Cadastro de Clientes](https://tdn.totvs.com/display/PROT/FAT0307+Compartilhamento+de+tabelas+relacionadas+ao+Cadastro+de+Clientes)
* [Recálculo de Comissões (FINA440 - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=312162528)

**Conciliador de Pagamentos e Vendas (FINA918):**

O compartilhamento das tabelas **SE1 e MEP** deve ser idêntico.

**Link Correspondente:**

[Conciliador Pagamentos e Vendas - Financeiro (Contas a Receber) - P12](https://tdn.totvs.com/display/PROT/Conciliador+Pagamentos+e+Vendas+-+Financeiro+%28Contas+a+Receber%29+-+P12)

**Comunicação Bancária - Retorno de Pagamento (FINA718):**

O compartilhamento das tabelas **F79 e F7A** deve ser idêntico.

**Link Correspondente:**

[Job de retorno dos pagamentos - FINA718](https://tdn.totvs.com/display/PROT/Job+de+retorno+dos+pagamentos+-+FINA718)

**Análise de Crédito Financeiro (FINAPP001):**

O compartilhamento das tabelas **F7F e SA1** deve ser idêntico.

**Link Correspondente:**

[Análise de crédito financeiro - FINAPP001 - Financeiro P12](https://tdn.totvs.com/pages/viewpage.action?pageId=720366867)

**Saiba mais**  
[Compartilhamento de tabelas do módulo Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=307830478)
