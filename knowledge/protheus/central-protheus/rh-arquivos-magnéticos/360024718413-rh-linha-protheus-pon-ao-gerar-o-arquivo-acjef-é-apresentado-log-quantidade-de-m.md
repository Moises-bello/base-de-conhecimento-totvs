---
article_id: 360024718413
category: RH - Arquivos Magnéticos
content_hash: 3fe96a0c2ab3b1eb3a43e432743459d5e7c3797e629f593daf4518d53f63ebaa
fetched_at: '2026-06-28T22:44:55.274199+00:00'
product: protheus
section_id: 32302371669783
source: central-protheus
title: 'RH - Linha Protheus - PON - Ao gerar o arquivo ACJEF é apresentado log: Quantidade
  de Modalidade de Hora Extra maior que 4'
type: support-article
updated_at: '2025-09-15T19:55:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024718413-RH-Linha-Protheus-PON-Ao-gerar-o-arquivo-ACJEF-%C3%A9-apresentado-log-Quantidade-de-Modalidade-de-Hora-Extra-maior-que-4
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34957925747607) Tempo aproximado para leitura: 00:01:00 min******Dúvida**Ao gerar o arquivo ACJEF é apresentado log: Quantidade de Modalidade de Hora Extra maior que 4  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Essa mensagem ocorre por dois motivos:

1 - Algum evento de Hora Extra gerado no período de apontamento, não está com o campo **Classificação** como Hora Extra no Cadastro de Eventos (Tabela SP9)

2 - Em algum dia do período, o sistema apontou mais do que 4 tipos de Hora Extra para o funcionário, sendo que ele não pode ter mais do que 4 tipos de H.E no dia de acordo com a portaria 1510, por exemplo:

Apontou em algum dia do período que está gerando:

H.E 50% Normal  
H.E 50% Noturna  
H.E 60% Intervalo Noturna  
H.E 60% DSR  
H.E 100% Feriado  
  
As tabelas relacionadas do ACJEF são: **RFF para período aberto** e **RFG para período já fechado.**  
Faça um filtro nas tabelas, pela filial que está apontando no log e pelo campo **RFF\_TIPOHE** ou **RFG\_TIPOHE,**diferente de (Branco). Avalie em qual dia consta mais do que 4 tipos de H.E diferentes apontado para ajuste. Após ajustar, retirando uma das H.E das tabelas, gere novamente o arquivo ACJEF  
  
**Importante:**  
Com a vigência da Portaria nº 671/2021, os arquivos AFDT e ACJEF foram substituídos pelo AEJ (Arquivo Eletrônico de Jornada). Os Programas de Tratamento de Registro de Ponto (PTRP), neste caso desta documentação o PTRP é o PROTHEUS módulo SIGAPON, se adequou até dia 11/01/2023 ao novo leiaute. Portanto, até o dia 10/01/2023, o PROTHEUS podia gerar os arquivos AFDT e ACJEF, conforme alteração trazida pela Portaria MTP nº 3.717, de 9 de novembro de 2022, que prorrogou o prazo estabelecido na Portaria MTP nº 671, de 8 de novembro de 2021. Porém, a partir desta data de 12/01/2023 o arquivo a ser gerado deve ser o AEJ.  
  
**Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Arquivo Eletrônico de Jornadas - AEJ - Portaria 671](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9326209981719-RH-Linha-Protheus-PON-Arquivo-Eletr%C3%B4nico-de-Jornadas-AEJ-Portaria-671)  
[RH - Linha Protheus - PON - AEJ gera log de Funcionários sem Marcações para Isentos de registro de ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21038601930519-RH-Linha-Protheus-PON-AEJ-gera-log-de-Funcion%C3%A1rios-sem-Marca%C3%A7%C3%B5es-para-Isentos-de-registro-de-ponto)  
<https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/fiscalizacao-do-trabalho/Perguntas%20e%20Respostas%20REP>
