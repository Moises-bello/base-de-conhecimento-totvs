---
article_id: 11169895277207
category: MDT - EPI
content_hash: 5e26ae3490c9420fb4448c58b733a518f3719de9ef4ba59f1bef80269d8d5a87
fetched_at: '2026-06-28T22:44:25.307170+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Como configurar o uso da Biometria no SIGAMDT
type: support-article
updated_at: '2024-02-20T19:19:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11169895277207-RH-Linha-Protheus-MDT-Como-configurar-o-uso-da-Biometria-no-SIGAMDT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20140184127255) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como configurar o uso da Biometria no SIGAMDT?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Após instalação do aparelho biométrico, conforme orientação [Como efetuar a instalação do aparelho FingerTech para Biometria no MDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11169209683991)   
Será necessário configurar os parâmetros:  
  
No módulo **Configurador**, acesse o caminho **Ambiente - Cadastros - Parâmetros** e localize os parâmetros, por exemplo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11169564854679)  
  
E configure os parâmetros abaixo conforme a coluna **Conteúdo**:

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Descrição** | **Conteúdo** |
| MV\_BIOMDT | Indica utilização de reconhecimento biométrico no produto SIGAMDT. Informe 1 para utilização com SmartAgent legado e 2 para FingerTech. | 2 |
| MV\_NG2BIOM | Indica se utiliza Biometria na Entrega de EPI. Informe 1=Sim ou 2=Não. | 1 |
| MV\_NG2RECI | Determina se apresentará sugestão de impressão do recibo de entrega de EPI.  1=Sim ou 2=Não. | 1 |
| MV\_DEVBIOM | Indica se utiliza Biometria na Devolução do EPI. Informe 1=Sim ou 2=Não. | 1 |
| MV\_NG2HOST | Host de conexão utilizado no módulo SIGAMDT. Caso a porta utilizada seja a 9000, manter o conteúdo vazio.  Observação: Por default o parâmetro é reconhecido quando é utilizado localhost:9000. | http://localhost:9000 |

Antes de iniciar o processo Biométrico, é necessário sempre iniciar o aplicativo **FingerTechWeb** ![](https://tdn.totvs.com/download/thumbnails/712475862/image2022-9-27_10-39-47.png?version=1&modificationDate=1664285988773&api=v2), ele deve ser apresentado na barra de tarefas do Windows.   
  
Após efetuar todas configurações, é o momento de cadastrar a Biometria do funcionário. No módulo Medicina e Segurança do Trabalho (35), acesse a rotina **Atualizações - Atendimento Médico - Ficha Médica** (MDTA005) selecione o funcionário e clique em **Alterar**, verifique se o campo **Biometria** (TM0\_INDBIO) esta igual a 1-Sim:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11169694207639)  
  
Na tela inicial da rotina **Ficha Médica**, posicione em cima do funcionario no qual irá cadastrar a biometria e clique no botão **Outras Ações > biometria**:    
  
![depois.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21489869987479)  
  
Nesse momento é aberta a tela para configurar a biometria para o funcionário:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11169818918935)

Também é possível fazer o processo de inclusão de digitais pela rotina de **Prontuário Médico (MDTA410)**, no menu Atualizações - Atendimento Médico - Prontuário Médico.  
  
A configuração é a mesma informada na Ficha Médica.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11169852483607)  
  
Caso seja necessário incluir uma nova digital ou alterar a digital já cadastrada, selecionar para alterar a ficha médica e ir em **Outras Ações - Biometria** e no questionamento abaixo, selecionar a opção Sim:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11169856242711)  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Como efetuar a instalação do aparelho FingerTech para Biometria no MDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11169209683991)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
