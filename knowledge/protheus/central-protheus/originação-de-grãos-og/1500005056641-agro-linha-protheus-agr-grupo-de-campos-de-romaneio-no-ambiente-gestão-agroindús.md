---
article_id: 1500005056641
category: Originação de Grãos (OG)
content_hash: 972fdbaa73bebdf8f022e7eedc9eb19691a115a7451af9cd80835b11f93e52c1
fetched_at: '2026-06-28T22:45:39.603898+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Grupo de campos de Romaneio no ambiente Gestão
  Agroindústria
type: support-article
updated_at: '2025-06-24T14:28:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005056641-Agro-Linha-Protheus-AGR-Grupo-de-campos-de-Romaneio-no-ambiente-Gest%C3%A3o-Agroind%C3%BAstria
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20355387992087)***Tempo aproximado para leitura:**00:01:30 min**  
**Dúvida**Qual o grupos de campos de **Romaneio** no ambiente **Gestão Agroindústria**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para melhor atender as necessidades dos clientes, foi criado o novo grupo de campos, com o **código 143**, para abranger todos os campos que fazem referencia ao **código de romaneio**. Devido a problemas com truncamento, será permitido o tamanho mínimo de 10 posições e o máximo de 20 posições.  
Os campos que serão afetados por essa melhoria são apenas aqueles que são utilizados pela regra da **Originação**.  
  
Segue a relação dos campos abaixo:  
**N7S - Instrução Embarque x Regra Fis** - campo - **N7S\_CODROM**  
**N89 - Relação Comissão Agro** - campo - **N89\_CODROM**  
**N8H - Vinculo Pedido Venda** - campo - **N8H\_CODROM**  
**N8I - Vinc.Itens Doc.Saida Sigaagr**  - campo - campo **N8I\_CODROM**  
**N8J - Vinculo docto de Saida Sigaagr** - campo - **N8J\_CODROM**  
**N8K - Vinc.Itens Doc.Saida Sigaagr**  - campo - **N8K\_CODROM**  
**N8L - Vinculo Titsa Receber Sigaagr**  - campo - **N8L\_CODROM**  
**N8M - Vinculo Tits a Pagar SigaAgr** - campo - **N8M\_CODROM**  
**N8Q - Blocos do Pré-Agendament**o  - campo - **N8Q\_CODROM**  
**N8T - Romaneio X Precificação**  - campo - **N8T\_CODROM**  
**N9A - Regras Fiscais do Contrato**  - campo - **N9A\_CODROM**  
**N9C - Itens da pendência** - campo - **N9C\_CODROM**  
**N9D - Movimentação de Fardos** - campo - **N9D\_CODROM**  
**N9E - Integração Romaneio** - campo - **N9E\_CODROM**  
**N9G - Panel de Previsão Financeira** - campo - **N9G\_CODROM**  
**N9I - Rem. Form. Lote x IE** - campo - **N9I \_CODROM**  
**N9K - Romaneio x Previsões** - campo - **N9K\_CODROM**  
**N9M - Amarração de compensação** - campo - campo **N9M\_CODROM**  
**N9R - Integração Retorno GFE**  - campo - **N9R\_CODROM**  
**NC8 - Pendências do Romaneio** - campo - **NC8\_CODROM**  
**NCN - Monitoramento** - campo - **NCN\_CODROM**  
**NJB - Controle de Reserva** - campo - **NJB\_CODROM**  
**NJJ - Romaneios** - campo - **NJJ\_CODROM**  
**NJK - Classificacoes do Romaneio** - campo - **NJK\_CODROM**  
**NJM - Dados Fiscais do Romaneio** - campo - **NJM\_CODROM**  
**NK4 - Histórico Classif. do Romaneio** - campo - **NK4\_CODROM**  
**NKC - DOCTOS AJUSTE DIFS. NA FIXACAO** - campo - **NKC\_CODROM**  
**NKG - Movimentos Servicos do Contrat** - campo - **NKG\_CODROM**  
**NKK - Liquidações da OP/OR**  - campo - **NKK\_CODROM**  
**NKS - Fechamento Servico**s  - campo - **NKS\_CODROM**  
**NNC - Fixacao x Entregas** - campo - **NNC\_CODROM**  
**NNW - Alteracao do Contrato** - campo - **NNW\_CODROM**Outros campos com o sufixo **CODROM - Código do romaneio** não pertencem as regras de negócio do **Originação**, sendo assim, a não alteração dos demais campos não provocará problemas de integridade a base de dados.  
  
**Importante**Todas as tabelas utilizadas em seu processo devem estar de acordo. Além das mais usuais mencionadas, para consultar tabelas envolvidas em cada rotina utilizada: pode ser verificado ao digitar o **F1 - Help de campos** de seu teclado, no *Help Online* da rotina estando seu *Help Online* configurado, expandindo a pasta **Dados Técnicos Tabelas**.  
Caso realize as validações e ainda ocorra o problema, será necessário solicitar auxilio da **Consultoria Totvs**. O **Suporte** não valida mais de duas decimais, realiza o teste no padrão nativo ou suporte investigativo para que acesse remotamente a sua base, visando avaliação *debug* da rotina para investigá-la e identificar a origem do problema.  
Para a consultoria *in loco* solicitar diretamente à seu **Gerente de atendimento TOTVS**.
