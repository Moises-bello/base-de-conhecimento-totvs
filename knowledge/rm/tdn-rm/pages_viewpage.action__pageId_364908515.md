---
content_hash: 2ea05b72dc7911ae3f4941100240f0ae50cde3136208c6b1259d0eb79c05016e
fetched_at: '2026-06-29T00:08:59.621129+00:00'
page_id: '364908515'
product: rm
source: tdn-rm
title: S-2260 – Convocação para Trabalho Intermitente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908515
version: 19
---

S-2260 – Convocação para Trabalho Intermitente

* Este evento tem como objetivo registrar a convocação para prestação de serviços do empregado com contrato de trabalho intermitente. Visa, portanto, formalizar e informar ao eSocial os termos pré-pactuados de cada convocação para prestação de serviços. Quem está obrigado: o empregador, sempre que ocorrer a convocação do empregado para a prestação de serviços de natureza intermitente. Este evento é exclusivo para trabalhadores admitidos com Categoria [111] – “Empregado com Contrato de Trabalho Intermitente”.
* Deve ser enviado antes do início da prestação de serviços para a qual o empregado está sendo convocado. Pré-requisitos: envio do evento S-2200 – Cadastramento Inicial e Admissão/Ingresso de Trabalhador.

Procedimentos para geração do evento S2260 – Convocação para Trabalho Intermitente

1º Passo: Realize o cadastro de uma convocação através do menu Administração de Pessoal | Funcionários | Movimento | Convocação para Trabalho Intermitente.

\_

Será gerado gatilho na fila de eventos para o evento S-2260 com status 0-pendente.

2ºPasso:Gerar XML:

O usuário deverá processar a  Geração do  XML para que o evento fique no status 1-Gerado .

Para isso deverá selecionar o evento e clicar Gerar XML dentro da fila de eventos ou através do menu esocial | Eventos de tabelas |Não Periódicos | Gerar XML.

3ºPasso:Integrar evento com o TAF

Realizar o processo de Integração do evento com o TAF:

Para isso deverá selecionar o evento e clicar Integrar TAF.

Neste momento o status do evento será alterado para 3-Enviado  para o TAF.

4ºPasso:Enviar os eventos gerados na fila para o Totvs Automação Fiscal (TAF):

5ºPasso: Atualizar status da integração TAF:

Para atualizar o status da integração do TAF terá as seguintes opções: Na fila de eventos selecionar   " Processos" |Atualizar Status integração TAF ou através do menu Processos | Atualizar Status Integração TAF.

Veja mapeamento dos campos que serão informados:
