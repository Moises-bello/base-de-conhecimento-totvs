---
content_hash: be3b8c9d480596a70b853fb6f25382e2d7f222ae0cb0dd45ed793411c74cde1e
fetched_at: '2026-06-29T00:09:14.945199+00:00'
page_id: '421385312'
product: rm
source: tdn-rm
title: Custos do Período 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385312
version: 2
---

---

Os apontamentos de equipamentos realizados pelo coletor móvel vão para o SIGAMNT (Protheus – Manutenção de Ativos), onde os custos diretos e indiretos dos equipamentos são agrupados e enviados para TOTVS Obras e Projetos para apropriação, rateio e revaloração. Também são enviados ao TOP todos os apontamentos realizados.

O envio dessas informações do SIGAMNT para o TOP ocorre através da rotina Miscelânea > Mensagem Única > Envio de Custo Mensal do SIGAMNT.

Os apontamentos e os custos diretos (das horas trabalhadas) serão agrupados por Filial/Equipamento/Ano-Mês/Frente de Trabalho.

Já os custos indiretos (manutenção corretiva, preventiva, abastecimento e outros) serão agrupados por Filial/Equipamento/Ano-Mês.

Através do menu Cadastros | Mobilidade | Equipamentos | Custo do Período | Custos Indiretos ou Cadastros | Mobilidade | Equipamentos | Custo do Período | Custos Diretos é possível visualizar todas as informações recebidas do Manutenção de Ativos.

**Atenção:**

As informações recebidas, não necessariamente, existem na base de dados do TOP uma vez que são provenientes de outro sistema, neste caso o SIGAMNT.

Por este motivo, caso seja encontrada alguma inconsistência, o sistema irá salvar uma mensagem explicativa sobre a inconsistência encontrada no campo Observação.

O processo não será abortado. O envio dos custos dos equipamentos para o TOP ocorre através da mensagens únicas "AssetMonthlyDirectCosts" (custos diretos) e "AssetMonthlyUndirectCosts" (custos indiretos).

O Manutenção de Ativos envia a mensagem ao TOP com os custos dos equipamentos.

O TOP valida e interpreta a mensagem, armazenando os custos para posterior apropriação e revaloração.

O TOP retorna ao Manutenção de Ativos uma sinalização de sucesso ou erro.

Durante a apropriação/revaloração no caso de existir mais de um insumo vinculado à família do bem que está no apontamento, a apropriação vai ser realizada para o primeiro insumo encontrado.

Caso não encontre nenhum insumo a partir do bem, não será realizada a apropriação e será informado no log de erros.
