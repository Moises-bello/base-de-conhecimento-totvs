---
content_hash: fed07871267551d00cdd4691b34f77f41c6c78a663b4a0ced8be9f292d5e6f96
fetched_at: '2026-06-29T00:08:44.821303+00:00'
page_id: '309402778'
product: rm
source: tdn-rm
title: RMFIS00006_Rendimentos pagos a residentes ou domiciliados no Exterior
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00006_Rendimentos+pagos+a+residentes+ou+domiciliados+no+Exterior
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Fiscal |
| **Versões:** | 12.x |
| **Ocorrência:** | Rendimentos pagos a residentes ou domiciliados no Exterior |
| **Ambiente:** |  |
| **Passo a passo:** | Os lançamentos de Rendimentos pagos a residentes ou domiciliados no exterior serão controlados exclusivamente pelo RM Liber.  Para que os lançamentos de Rendimentos pagos a residentes ou domiciliados no exterior sejam gerados, é necessário marcar o campo “Declarante de rendimentos pagos a residentes ou domiciliados no exterior” (segunda etapa da tela de Geração da DIRF):                                  Filtros utilizados:     * Somente serão selecionados os Lançamentos que no ato da Baixa acumularam valor para o Tributo “IRRF Importação”. Caso existam outros tributos nos Lançamentos selecionados, os mesmo serão ignorados, visto que somente devem ser destacados na DIRF o IRRF de Importação.  * Lançamentos que não estejam cancelados;  * Lançamentos que não sejam extemporâneos;  * Lançamentos que não sejam estornados;  * Lançamentos de Entrada;  * Lançamentos em que o Fornecedor seja do Tipo Emitente (Campo da tela do Lançamento Fiscal) seja “Empresa” ; * Lançamentos que não sejam Notas Fiscais que acobertam Cupom Fiscal ; * Lançamentos que possuam o Tributo IRRF Importação;  * Deverão estar informados os campos de “País” e “Estado” na aba de Endereço do Cadastro de Cliente/Fornecedor. Somente serão retornados Lançamentos em que o Estado do Cliente/Fornecedor não esteja com a opção “Nacional” marcada;  * Para que os Lançamentos referentes aos Fornecedores do Exterior sejam gerados, também é necessário preencher o campo “Data do Desembaraço Aduaneiro” (Informações Adicionais, aba “Importação”):      * Para que os Lançamentos referentes aos Fornecedores do Exterior sejam gerados, também é necessário preencher o campo “Data Vencimento” (Integrações, aba “Dados Financeiro”):            * Para que os Lançamentos referentes aos Fornecedores do Exterior sejam gerados, também é necessário criar o Relacionamento entre os Participantes da operação, no Cadastro de Cliente/Fornecedor, Anexo “Participante – SPED Contábil”:        * No cadastro do tributo o código de receita deve estar preenchido; * No cadastro do cliente fornecedor o Número do NIF, Situação do NIF, Forma de Rendimento e Forma de tributação devem estar informados; Obs.: A forma de tributação o sistema verifica primeiramente no lançamento fiscal no tributo IRRF Importação. Caso esteja como Nenhuma Forma de Tributação Definida, o sistema irá verificar no cadastro do cli/for. |
| **Observações:** |  |
