---
content_hash: c044ce7d2daaac2962067d06ece6218fbaad0b90d6431ea5f5529fbc5c6459ef
fetched_at: '2026-06-29T00:11:38.252792+00:00'
page_id: '782315485'
product: rm
source: tdn-rm
title: Quais autônomos do TOTVS Gestão Financeira são considerados na geração do S-1200
  e S-1210?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=782315485
version: 18
---

false

**A partir das Versões:**

* + 12.1.2209
  + 12.1.2302
  + 12.1.2306

# Objetivo:

---

Detalhar quais autônomos do produto TOTVS Gestão Financeira são incorporados no processo de geração dos eventos S-1200 e S-1210 do eSocial, a fim de assegurar que o usuário possa verificar a exatidão das informações.

O sistema TOTVS Folha de Pagamento utiliza as seguintes regras para buscar os autônomos no sistema TOTVS Gestão Financeira (RM Fluxus):

* O autônomo (cliente fornecedor) deve ser uma pessoa física;
* O tipo de documento deve ser um dos seguintes: Gera INSS, Gera INSS e IRRF ou Gera IRRF;
* O status do lançamento não pode ser "Cancelado";
* No lançamento, é necessário que haja desconto de IRRF ou INSS.
* Caso o campo "código categoria" nos anexos do Cliente/Fornecedor no eSocial não esteja preenchido, isso resultará na não geração dos eventos S-1200 e S-1210. Essa medida é para evitar a duplicação de autônomos no REINF.

**ATENÇÃO I:** Para Produtor Rural e MEI, existem algumas particularidades.

Veja mais detalhes em:

**A****TENÇÃO II:** Para transportador além das considerações acima, também é verificada as categorias.

Veja mais detalhes em:

**A****TENÇÃO III:** Para transportador além das considerações acima, também é verificada as categorias.

**ATENÇÃO IV:** Não é possível ter um mesmo vínculo (categoria) para o mesmo CPF, registrado como autônomo, nos produtos TOTVS Folha de Pagamento e TOTVS Gestão Financeira, quando ambos estão ativos sob o mesmo CNPJ.

**ATENÇÃO V:**

No que diz respeito ao INSS, o REINF não considera os autônomos do setor Financeiro, apenas do Fiscal.

Em relação ao IRRF, os autônomos incluídos no REINF podem ser verificados no seguinte link, mediante coordenação com a Denise.

É importante ressaltar que, atualmente, a responsabilidade de incluir autônomos no REINF está nas mãos do usuário, que decide quais autônomos serão registrados.
