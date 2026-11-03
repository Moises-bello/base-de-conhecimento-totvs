---
content_hash: abe3ef8ae81d4260df40306f83ba26ef0143871e707598d4d7975a9901015534
fetched_at: '2026-06-29T00:09:52.889069+00:00'
page_id: '439696890'
product: rm
source: tdn-rm
title: DT - Liberar adiantamento ou retenção gerando título / pedido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439696890
version: 11
---

# LIBERAR ADIANTAMENTO OU RETENÇÃO GERANDO TÍTULO / PEDIDO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Obras e Projetos |
| **Função:** | Liberar Adiantamento / Liberar Retenção |
| **Situação/Requisito:** | Permitir gerar um pedido no back-office no lugar de um título financeiro ao liberar um adiantamento ou uma retenção em contratos. |
| **Solução/Implementação:** | O TOTVS Obras e Projetos passa a permitir gerar um pedido de compra no back-office ao liberar um adiantamento ou uma retenção de um contrato.  Foi adicionado o parâmetro "Liberar Adiantamento ou Retenção" nos parâmetros de projeto em "Integração | Suprimentos / Faturamento | Geral" com as seguinte opções:   * Título Financeiro a Pagar / Receber - Com esta opção marcada o sistema mantém o processo padrão, gerando um título financeiro na liberação do adiantamento ou retenção. No processo de "Gerar Integração com Suprimentos / Faturamento" o comportamento não foi modificado; * Pedido de Compra / Venda - Opção disponibilizada para gerar um pedido de compra na liberação do adiantamento ou retenção. Sendo que no processo de "Gerar Integração com Suprimentos / Faturamento" a lista de documentos de créditos não será enviada no caso de liberação de adiantamento será enviado como desconto.      Atenção:  * Disponível somente quando integrado com back-office PROTHEUS utilizando a integração via EAI. * Houveram ajustes na integração por mensagem única (EAI 1.0), sendo necessário a manutenção na transformação da mensagem ORDER e em seguida a execução do configurador da integração. Recomendamos o apoio do suporte técnico para esta etapa caso não possua o conhecimento necessário. |
| **Conversores e Parâmetros:** | Parâmetro de projeto: |
| **Tickets relacionados:** | Não se aplica. |
| **Requisito:** | TOPEXECONTROL01-4947 / TOPEXECONTROL01-4950 / TOPEXECONTROL01-4949 |
| **Documento de Referência:** | Não se aplica. |
| **Pacote:** | Não se aplica. |
