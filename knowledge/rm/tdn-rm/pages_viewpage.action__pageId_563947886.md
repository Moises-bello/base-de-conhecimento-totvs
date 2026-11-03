---
content_hash: 8ff4fb3a73a8df89fd3dc2c51a066d61d017656a907de19fa6bf53d06d373524
fetched_at: '2026-06-29T00:10:51.220298+00:00'
page_id: '563947886'
product: rm
source: tdn-rm
title: Corretores - Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563947886
version: 7
---

## Editar a comissão da proposta

O Portal de Imóveis pode atribuir automaticamente a comissão do corretor que gerou a venda, mas para isto é necessário ter o percentual de comissão definido. O Portal possibilita que a comissão seja calculada pelo Empreendimento, Usuário, Imobiliária ou grupo de usuário, nesta ordem de precedência, ou seja, se definida uma comissão no cadastro do empreendimento esta irá sobrepor todas as demais.

Uma comissão pode ter seu valor lançado manualmente após proposta feita e entrando no menu de ações da proposta opção COMISSÃO (esta opção só aparece para propostas aprovadas). Ou calculada automaticamente pelo Portal de Imóveis baseado nos percentuais definidos no parágrafo acima. Para isto o parâmetro "Grava Comissão Diretamente" deve estar marcado como SIM.

Se marcado como SIM ao salvar uma proposta o sistema criará automaticamente um valor de comissão. O Portal de Imóveis trata o percentual de comissão definido como sendo o teto de comissão a pagar, não permitindo lançar um valor maior que o definido pelo percentual aplicado aos componentes que estão com o FLAG de descontar comissão habilitados.

A comissão é calculada sobre o valor total da proposta multiplicando sobre o percentual da comissão do empreendimento, ou do usuário, ou da imobiliária ou do grupo do usuário, se todos estes campos estiverem zeramos o valor base de comissão e o valor da comissão serão zero.

Caso a soma das parcelas que permitem descontar comissão (Flag demonstrado na imagem) não seja suficiente para pagar toda a comissão calculada, o valor da comissão será limitado no valor do componente que está marcado com Desconta Comissão.

É possível distribuir a comissão entre mais de um usuário, desde que esta não ultrapasse o teto permitido. Para lançar outras pessoas participantes da comissão basta inserir novos usuários clicando em ADICIONAR LINHA DE COMISSÃO.

OBS: No Portal de Imóveis existem parâmetros que permitem que o sistema calcule ou não o valor da comissão automaticamente e parâmetros que definem se uma proposta poderá avançar para próxima etapa sem comissão lançada. Para modificar estes parâmetros acesse Backend e em pesquisa de parâmetros a palavra COMISSÃO. Os parâmetros são:

* Grava comissão diretamente - para que o sistema já gere um valor de comissão para as propostas salvas
* Permitir efetivar propostas sem comissão - permite ou não que uma proposta avance para próxima etapa sem comissão gerada.
