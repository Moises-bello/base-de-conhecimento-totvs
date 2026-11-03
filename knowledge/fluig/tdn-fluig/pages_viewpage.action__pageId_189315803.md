---
content_hash: 94ac3298170b2539d57f64a6c1a3222a476e602709f685db47a0b4f83607f8d9
fetched_at: '2026-06-28T21:35:19.080952+00:00'
page_id: '189315803'
product: fluig
source: tdn-fluig
title: MOB - Por que o IOS continua mostrando as casas decimais de uma planilha com
  formatação personalizada de células?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=189315803
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** Fluig Mobile

# Ocorrência

Quanto tento visualizar uma planilha com formatação personalizada nas células de valor para não exibir as casas decimais no iOS, as casas são exibidas.

# Solução

As casas decimais dos números são exibidas no iOS porque o visualizador utilizado pelo sistema (iOS) não consegue respeitar a formatação personalizada da célula. Esse não é um problema com o Fluig Mobile, pois a visualização não ocorre internamente em ambiente mobile.   
Se você tentar visualizar o mesmo documento em um Android por exemplo, o documento será baixado para o aparelho e o Android utilizará o aplicativo mais adequado para abrir o documento. Se esse aplicativo conseguir respeitar a formatação personalizada, as casas decimais não são exibidas.
