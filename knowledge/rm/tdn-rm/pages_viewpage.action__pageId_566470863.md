---
content_hash: ad55c4923375476ac8c89e9d4133277e8d9e4ab33e4b7401e3e88b2826d42ac6
fetched_at: '2026-06-29T00:10:51.325740+00:00'
page_id: '566470863'
product: rm
source: tdn-rm
title: Portal de Imóveis - Frontend - Corretores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=566470863
version: 10
---

**Importante!**  
Ao realizar uma proposta, o corretor poderá selecionar a imobiliária atual no campo Imobiliária, mas por padrão será auto selecionado a imobiliária definida no cadastro do usuário.  
Esta informação será gravada no momento em que a proposta é feita. Desta forma o Portal de Imóveis consolida um histórico de imobiliárias que o corretor pertence ou pertencia no momento em que a proposta foi realizada.

**Relatórios gerenciais**

---

É importante notar que o campo *imobiliaria\_proposta (imobiliária\_id)* da tabela *proposta*será o responsável pelo armazenamento das informações a respeito deste histórico de imobiliárias. Abaixo, segue um exemplo de *select* onde extraímos esta informação diretamente do banco.

Usamos o comando **COALESCE** para buscar primeiro em proposta se houver valor para imobiliária, se existir, este será o valor a ser considerado, caso não exista aí buscamos a imobiliária vinculada ao usuário. Vale lembrar que isso é para manter compatibilidade com as propostas antigas, a partir da nova versão, se houver imobiliária ela sempre estará disponível na proposta.
