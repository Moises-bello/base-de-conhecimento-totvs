---
content_hash: 3c1a64895f20d694c2068453d44b13097b84ce9063859b1ff9262d91725ed296
fetched_at: '2026-06-29T00:09:02.409502+00:00'
page_id: '379306873'
product: rm
source: tdn-rm
title: 2801501 MATFATCMPCRM01-3626 DT - Cancelamento de Movimento via Web Service
type: documentation
url: https://tdn.totvs.com/display/LRM/2801501+MATFATCMPCRM01-3626+DT+-+Cancelamento+de+Movimento+via+Web+Service
version: 6
---

# Cancelamento de Movimento via WebServices

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Cancelamento de Movimento |
| **Situação/Requisito:** | Durante o processo de cancelamento de movimento, o usuário precisa tomar algumas decisões em situações específicas. O Sistema não permitia tomar estas decisões durante o cancelamento via WebService. |
| **Solução/Implementação:** | Foram criadas 3 novas Tags no XML de cancelamento de movimento via WebService, são elas:   * Durante o processo de faturamento existe a opção de gerar N movimentos de destino (Quebra de Movimento). Ao cancelar um destes registros o sistema pergunta se o usuário gostaria de cancelar todos os movimentos gerados simultaneamente, caso seja selecionada a opção "Sim", o cancelamento é feito para todos os registros gerados pelo processo, caso contrário o cancelamento é abortado.  Foi criada a tag **CancelarMovimentosGeradosSimultFaturamento,** a qual é responsável por esta decisão durante o cancelamento via WebService. * Ao cancelar um movimento gerado através de cotação, onde a mesma NÃO esteja parametrizada para "Permitir Cotação Parcialmente Gerada" e, durante o processo de geração de ordem de compra foram gerados N registros, o sistema pergunta se o usuário deseja cancelar os movimentos gerados simultaneamente, caso seja selecionada a opção SIM, todos os registros serão cancelados e a cotação será reaberta, caso seja selecionada a opção NÃO, o sistema informa que os itens que deram origem a este movimento serão excluídos da cotação e pergunta se o processo deve ser executado, caso o usuário selecione a opção SIM, o produto é excluído da cotação, caso contrário o processo é abortado. Foi criada a tag **CancelarMovimentosGeradosSimultReabriCotacao**, a qual é responsável por definir se todos os movimentos gerados simultaneamente devem ser cancelados e a cotação reaberta. Foi criada a tag **ExcluirItensDaCotacao**, a qual é responsável por definir se os itens que deram origem a este movimento devem ser excluídos da cotação.     **RMSProcess**: MovCancelMovProc  **Exemplo de XML:**  <MovimentosACancelar>  <MovimentosCancelar z:Id="i3">  <ApagarMovRelac>false</ApagarMovRelac>  **<CancelarMovimentosGeradosSimultFaturamento>true</CancelarMovimentosGeradosSimultFaturamento>**  **<CancelarMovimentosGeradosSimultReabriCotacao>false</CancelarMovimentosGeradosSimultReabriCotacao>**  <CodColigada>1</CodColigada>  <CodSistemaLogado>T</CodSistemaLogado>  <CodUsuarioLogado>mestre</CodUsuarioLogado>  <DataCancelamento>2018-07-31T00:00:00-02:00</DataCancelamento>  **<ExcluirItensDaCotacao>true</ExcluirItensDaCotacao>**  <IdExercicioFiscal>22</IdExercicioFiscal>  <IdMov>5285</IdMov>  <MotivoCancelamento></MotivoCancelamento>  <NumeroMov i:nil="true" />  </MovimentosCancelar>  </MovimentosACancelar>  </MovCancelMovProcParams> |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 2801501 |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
