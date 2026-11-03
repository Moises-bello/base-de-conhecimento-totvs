---
content_hash: dac99d6f2b94bc1b5613dbf216524262c83f50232e77509ef78f59edac2207ec
fetched_at: '2026-06-29T00:05:55.915629+00:00'
page_id: '147816869'
product: rm
source: tdn-rm
title: 'Erro ao gerar Homolognet: "Não é possível definir a coluna ''DSComplemento''.
  O valor viola o limite de MaxLength desta coluna."'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=147816869
version: 1
---

| Produto | **RM** |
| --- | --- |
| **Sintoma** | **Erro ao gerar Homolognet: "Não é possível definir a coluna 'DSComplemento'. O valor viola o limite de MaxLength desta coluna."**  \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  **Processo finalizado com erros!** |
| Solução | O erro ocorre pois no momento da geração do homolognet, o sistema valida o campo complemento de endereço da seção centralizadora do funcionário. Caso este campo possua muitos caracteres ou espaços inválidos o sistema irá apresentar o erro, para isso basta eliminar os espaços e/ou diminuir a quantidade de caracteres. |
