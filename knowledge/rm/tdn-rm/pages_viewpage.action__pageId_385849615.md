---
content_hash: 1b5bc081eddf8e0b1fe7e1b582f2721ab06f73207e7dd56643837fe7d0c9785a
fetched_at: '2026-06-29T00:09:07.796294+00:00'
page_id: '385849615'
product: rm
source: tdn-rm
title: 3316703 FOPROTINAS01-5235 Cadastro de Férias Partidas portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385849615
version: 1
---

# Férias partidas permitindo cadastras mais de uma sugestão com a opção de "Pagar 1ª parcela 13º"

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Recursos Humanos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Sugestão de Férias |
| **Situação/Requisito:** | Ao incluir sugestão de férias partidas no portal mantendo o parâmetro ‘ Pagar 1ª parcela do 13º’ marcado nas sugestões, o sistema está calculando o adiantamento da 1ª parcela indevidamente para todos os períodos sugeridos. |
| **Solução/Implementação:** | Para esta demanda foi ajustado para que não seja possível cadastrar mais de uma sugestão com a opção de "Pagar 1ª parcela 13º" caso o mesmo esteja compreendido em um ano cujo a solicitação ja tenha sido realizada   * **RM:**   Período Aquisitivo    1ª Sugestão: Solicitação para pagamento da 1ª Parcela 13º    2ª Sugestão: Solicitação para pagamento da 1ª Parcela 13º     * Será exibido a mensagem informando que a "1ª Parcela de 13ª salário" já foi solicitada em outro Período de Gozo      * Caso continue o cadastro o período será salvo e ira aparecer a informação adicional no Período de Gozo conforme abaixo      * Após lançar e a situação de Férias estiver “Pagas”, o aviso não irá mais ser exibido para este período de Gozo      * Ao editar outro período que não esteja com situação das Férias “Pagas” e já houve a solicitação para “Pagar 1ª parcela 13º” irá ser exibido em informações adicionais a mensagem conforme abaixo.      * **Portal:**   1ª Sugestão VIA Portal: Solicitação para pagamento da 1ª Parcela 13º      2ª Sugestão VIA Portal: Solicitação para pagamento da 1ª Parcela 13º      2ª Sugestão VIA Portal: Sem a Solicitação para pagamento da 1ª Parcela 13º |
| **Tickets relacionados:** | 3316703 |
