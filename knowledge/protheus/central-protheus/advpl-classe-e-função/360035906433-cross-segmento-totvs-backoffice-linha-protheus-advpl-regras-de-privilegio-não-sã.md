---
article_id: 360035906433
category: ADVPL - Classe e Função
content_hash: 4b224666e3ce9211a066f36ac3bf90c128db504e4c20301306c6d9f92e4a66da
fetched_at: '2026-06-28T22:40:17.138181+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Regras de Privilegio
  não são acatadas em rotina customizadas
type: support-article
updated_at: '2021-07-06T20:34:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035906433-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Regras-de-Privilegio-n%C3%A3o-s%C3%A3o-acatadas-em-rotina-customizadas
---

**Dúvida**Na release P12.1.25 as rotinas customizadas não estão acatando as regras de privilégios?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão P12.1.25  
  
**Solução**Para que as regras de privilégios sejam acatadas em funções de usuário é necessário que o ponto de entrada esteja dentro do *menudef* ou seja mesmo que o aRotina esteja disponível para manipulação não significa que ele esteja no *menudef*.

Verifique também a estrutura do array pois o 4º parâmetro do *array* é de 1 caractere ou seja de 0 a 9

Sub menus também não acatam regras de privilégios.

```
aAdd(aRotina, {"Minha Funcao", "u_MinhaFuncao()", 0, 5})
```

**Saiba Mais**[Funções reservadas — MenuDef](https://medium.com/totvsdevelopers/fun%C3%A7%C3%B5es-reservadas-menudef-b875f6a49667)  
[MenuDef](https://tdn.totvs.com/display/public/PROT/MenuDef)
