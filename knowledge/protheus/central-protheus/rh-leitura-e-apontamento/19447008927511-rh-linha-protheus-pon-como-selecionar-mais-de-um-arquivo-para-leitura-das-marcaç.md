---
article_id: 19447008927511
category: RH - Leitura e Apontamento
content_hash: 61d8b5556ab8b336f4b429d6c19b50775cc11cc90c832ad9a937987ab1eab000
fetched_at: '2026-06-28T22:44:46.054983+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Como selecionar mais de um arquivo para Leitura
  das Marcações
type: support-article
updated_at: '2025-06-05T13:53:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19447008927511-RH-Linha-Protheus-PON-Como-selecionar-mais-de-um-arquivo-para-Leitura-das-Marca%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19447002032791) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como possibilitar a escolha de mais de um arquivo TXT para cada relógio selecionado na rotina de Leitura/Apontamento?  
  
**Ambiente**Microsiga Protheus – Ponto Eletrônico – Todas as versões  
  
**Solução**No **Configurador (SIGACFG)**, acesse **Ambientes-Cadastros-Parâmetros, filtre o** **MV\_FILTREL** caso ele esteja com conteúdo **'S'** habilita o botão **Filtrar** na interface da rotina de Leitura/Apontamento (PONM010), onde permite a seleção de um arquivo diferente ou mais de um arquivo para cada relógio.   
Ao clicar no botão **Filtrar,** o sistema vai apresentar todos os arquivos da pasta vinculada ao cadastro do relógio, para cada relógio selecionado através das perguntas Filial De/Até, Relógio De/Até e o tipo da leitura que será realizada (marcações, refeições ou acessos).  
  
Segue abaixo um exemplo de utilização:  
  
**>** Cadastro de Relógios, onde temos dois relógios para leitura de Marcações (Controle = P) e um para leitura de Refeições (Controle = R):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19447119911575)  
  
  
**>** Com o parâmetro **MV\_FILTREL = S**, o botão **Filtrar** é exibido na rotina de Leitura/Apontamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19447088986519)  
  
  
**>** O sistema vai utilizar as perguntas da rotina para definir quais relógios serão apresentados, filtrando por **Filial De/Até, Relógio De/Até** e o **tipo da leitura** que será realizada (marcações, refeições ou acessos). No exemplo abaixo, estamos selecionando a leitura de **Marcações** apenas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19447088999063)  
  
  
**>** Ao clicar no botão **Filtrar**, o sistema busca todos os arquivos presentes na pasta informada no cadastro dos relógios que farão leitura de Marcações, por exemplo, a pasta \RELOGIOS\REP 002, \RELOGIOS\REP 003 e assim sucessivamente:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19447089002519)  
  
  
- Mesmo com o relógio 004 filtrado, os arquivos dele não serão exibidos, pois ele trata apenas da leitura de Refeições;  
- Os arquivos vinculados aos relógios filtrados já são automaticamente selecionados, porém, podem ser desmarcados;  
- Não há limite de seleção, portanto, o usuário pode escolher quantos arquivos quiser;  
- A seleção deve ser realizada a cada processamento da rotina de Leitura/Apontamento, pois os arquivos selecionados não serão armazenados pelo sistema.  
  
**Saiba Mais:**  
[MV\_FILTREL](https://tdn.totvs.com/pages/releaseview.action?pageId=695201706)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
