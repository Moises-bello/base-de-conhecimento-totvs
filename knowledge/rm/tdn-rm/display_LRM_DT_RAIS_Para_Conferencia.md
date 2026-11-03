---
content_hash: a378cbe5f621914bf392fb2512bbf33079f839584f70e4bbfcc218c0145658bc
fetched_at: '2026-06-29T00:06:21.985638+00:00'
page_id: '223910008'
product: rm
source: tdn-rm
title: DT_RAIS_Para_Conferencia
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_RAIS_Para_Conferencia
version: 5
---

# RAIS PARA CONFERÊNCIA

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Anuais/RAIS* | *Gerar RAIS para conferência* | |
| **Versões/Release:** | *12.1.9 / 11.82* |

## Descrição

Este documento descreve os procedimentos necessários para geração do relatório RAIS para conferência no formato texto.

## Procedimento para Utilização

**Gerar relatório RAIS para conferência**

O TOTVS Folha de Pagamento tem a opção para gerar o relatório RAIS no formato texto para conferência. O relatório de conferência foi criado utilizando um relatório do Reports e deverá seguir  o mesmo layout da RAIS em formato texto gerado em Delphi.   
No menu RH | Folha de Pagamento | Anuais | Rotinas | RAIS, foi adicionado o campo ‘Gerar RAIS em txt’  e o Campo 'Código do Relatório' no Grupo box 'Gerar RAIS para Conferência’.

Para gerar , o usuário deve acessar o menu RH | Folha de Pagamento | Anuais | Rotinas | RAIS, informar um caminho para salvar o relatório (Campo ‘Localização do(s) Arquivo(s)’), marcar as opções ‘Gerar RAIS para Conferência’ e ‘Gerar RAIS em txt’, e selecionar o relatório FOPREL0013 - RAIS para conferência, clicar em avançar até executar o processo. Ao concluir o processo, o sistema irá gerar o relatório no formato texto no caminho informado e abrirá o arquivo gerado no formato .txt.

**Observações**

O campo  ‘Gerar RAIS em Txt’ somente ficará habilitado quando o campo ‘Gerar RAIS para Conferência’ estiver marcado;

O campo para seleção do relatório somente ficará habilitado quando o campo ‘Gerar RAIS em txt’ estiver marcado e quando habilitado o mesmo deverá ser obrigatório;

Este relatório estará disponível no repositório de objetos gerenciais no caminho padrão de instalação C:\totvs\CorporeRM\ObjetosGerenciais\Relatórios (este caminho pode ser variável conforme a instalação, por exemplo em ambientes 3 camadas).

Ao marcar o campo ‘Gerar RAIS em Txt’ o sistema deverá desmarcar o campo ‘Utilizar Layout criado pelo Usuário’ e juntamente limpar o campo ‘Layout’;

 Ao marcar o campo ‘Utilizar Layout criado pelo Usuário’ o sistema deverá desmarcar o campo ‘Gerar RAIS em txt’ e juntamente limpar o campo de ‘Relatório’.
