---
content_hash: 7b5fe37e521c1ce516a9eb56da4b1366bd5d78fca3260aa33c100babf06c541c
fetched_at: '2026-06-29T00:06:07.791449+00:00'
page_id: '201737922'
product: rm
source: tdn-rm
title: ER_PCREQ-6565_SAÚDE_CIH_FLUIG_12.1.9_CONSULTA RÁPIDA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201737922
version: 6
---

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS CIH | **Módulo** | Consultas Rápidas |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAÚDE\_CIH\_FLUIG | **IRM1** | PCREQ-6527 |
| **Requisito1** | PCREQ-6567 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

## Permitir de forma rápida que os responsáveis pelo Centro de Infecção Hospitalar comuniquem aos demais enfermeiros que o paciente necessita de isolamento devido o resultado de Cultura Positiva.

### (Obrigatório)

## Definição da Regra de Negócio

* Após selecionar um registro na lista de pacientes com Cultura Positiva e selecionar a opção “Alerta de Cultura Positiva”, o CIH apresentará uma tela onde o usuário informará qual o tipo de Isolamento deverá ser oferecido ao paciente e permitirá incluir Orientações para os enfermeiros responsáveis pela unidade.
* Ao confirmar as informações o CIH enviará um e-mail para a unidade que o paciente está internado.
* Os e-mails de cada unidade serão configurados conforme documento ER\_PCREQ-\_Saúde\_CIH\_Fluig\_12 1 9 Configurações.

## Protótipo de Tela

**Protótipo 01**

### Opcional

## Fluxo do Processo

1. O usuário responsável pelo CIH configura os e-mails para cada unidade existente no estabelecimento;
2. O usuário avalia os pacientes que possuem resultado de Cultura Positiva;
3. Responsável pelo CIH seleciona um registro na lista de pacientes com cultura positiva;
4. Informa o tipo de isolamento e as demais orientações;
5. O CIH envia e-mail para a unidade responsável com as orientações inseridas pelo responsável pelo CIH.

 

### Opcional

### (Opcional)

## Grupo de Perguntas

 

*<Informações utilizadas na linha Protheus>.*

 

**Nome: FINSRF2**

|  |  |
| --- | --- |
| **X1\_ORDEM** | 01 |
| **X1\_PERGUNT** | Emissão De |
| **X1\_TIPO** | D |
| **X1\_TAMANHO** | 8 |
| **X1\_GSC** | G |
| **X1\_VAR01** | MV\_PAR01 |
| **X1\_DEF01** | Comum |
| **X1\_CNT01** | '01/01/08' |
| **X1\_HELP** | Data inicial do intervalo de emissões das guias de DARF a serem consideradas na seleção dos dados para o relatório |

### (Opcional)

### (Opcional)

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
