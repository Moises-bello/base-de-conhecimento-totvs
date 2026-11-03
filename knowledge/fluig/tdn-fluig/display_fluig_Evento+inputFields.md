---
content_hash: a471837f3c40059e22b2521083e398637aa91384d703744831eb6809081ff79e
fetched_at: '2026-06-28T21:35:30.374160+00:00'
page_id: '849550639'
product: fluig
source: tdn-fluig
title: Evento inputFields
type: documentation
url: https://tdn.totvs.com/display/fluig/Evento+inputFields
version: 1
---

É disparado no momento em que os dados do formulário são passados para a camada de negócio responsável por formulário do Fluig e pode ser utilizado para fazer algumas transformações dos valores que são enviados a fim de evitar erros como o formato de data que podem variar conforme o navegador

jsSintaxe

# Propriedades do getValue

Neste método nenhum parâmetro do  está disponível

# Pontos de atenção

Este evento não é executado na "Movimentação em Bloco". Como o seu uso é para correções de informações vindas do navegador, e na movimentação em bloco isso não acontece ele não é executado.

# Exemplos de uso

## Padronização de datas

Exemplo de código que recupera uma data no formato **YYYY-mm-dd** e grava no formato **dd-mm-YYYY**

Hoje no sistema as datas salvas através de formulários pelo navegador Chrome tem o padrão americano (yyyy-mm-dd), enquanto as datas nos demais navegadores tem o padrão brasileiro (dd/mm/yyyy). Para empresas que utilizam múltiplos navegadores e querem que os dados de data estejam padronizados, recomendamos a utilização do evento *inputFields* com o seguinte trecho de código.

jsCódigo para Datas
