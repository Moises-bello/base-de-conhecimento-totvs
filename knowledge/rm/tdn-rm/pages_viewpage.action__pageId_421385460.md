---
content_hash: c48bfe79a8f5fb6e7d5214a4c9c302fc0bf1c2230e874d6bd597dd0d32c4386e
fetched_at: '2026-06-29T00:09:16.117733+00:00'
page_id: '421385460'
product: rm
source: tdn-rm
title: Importação dos Custos dos Equipamentos 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385460
version: 3
---

---

Os apontamentos de equipamentos realizados pelo coletor móvel vão para o SIGA-MNT (Protheus – Manutenção de Ativos), onde os custos diretos e indiretos dos equipamentos são agrupados e enviados para TOTVS Obras e Projetos para apropriação e revaloração. Também são enviados ao TOP todos os apontamentos realizados. Os apontamentos e os custos diretos (das horas trabalhadas) serão agrupados por Filial/Equipamento/Ano-Mês/Frente de Trabalho. Já os custos indiretos (manutenção corretiva, preventiva, abastecimento e outros) serão agrupados por Filial/Equipamento/Ano-Mês.  Através do menu Cadastros | Mobilidade | Equipamentos | Custos do Período é possível visualizar todas as informações recebidas do Manutenção de Ativos.

**Atenção:**

* As informações recebidas, não necessariamente, existem na base de dados do TOP uma vez que são provenientes de outro sistema, neste caso o SIGA-MNT. Por este motivo, caso seja encontrada alguma inconsistência, o sistema irá salvar uma mensagem explicativa sobre a inconsistência encontrada no campo Observação. O processo não será ser abortado;
* O envio dos custos dos equipamentos para o TOP ocorre através da mensagem única "AssetMonthlyCosts". O Manutenção de Ativos envia a mensagem ao TOP com custos dos equipamentos. O TOP valida e interpreta a mensagem, armazenando-a para posterior apropriação e revaloração. O TOP retorna ao Manutenção de Ativos uma sinalização de sucesso ou erro.
