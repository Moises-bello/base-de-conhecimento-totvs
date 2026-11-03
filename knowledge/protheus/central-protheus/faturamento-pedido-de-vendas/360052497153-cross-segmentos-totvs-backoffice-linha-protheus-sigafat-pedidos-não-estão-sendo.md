---
article_id: 360052497153
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1ffb0156329a70bf63bc74d2dd9e2672bac7ebca45ffa50e6f5f0cb54c080af7
fetched_at: '2026-06-28T22:38:41.157260+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pedidos não
  estão sendo apresentados no Browser da Tela de Pedidos de Venda
type: support-article
updated_at: '2021-11-05T15:58:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052497153-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pedidos-n%C3%A3o-est%C3%A3o-sendo-apresentados-no-Browser-da-Tela-de-Pedidos-de-Venda
---

**Ocorrência**

 Pedidos não estão sendo apresentados no Browser da Tela de Pedidos de Venda.  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT – todas as versões  
  
**Causa**

Este incidente ocorre devido algum procedimento que foi realizado na rotina, abaixo vou informar as principais recorrências;

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

**Campo Filial;**  
1. Acessar o Configurador (SIGACFG), Base de Dados >> Dicionário >> Bases de Dados;   
2. Localizar a tabela **"Pedido de Venda - SC5",** ir no campo C5\_FILIAL, verificar se ele está na primeira Ordem da tabela, e se na Aba **"Uso"**, não tem nenhum registro marcado;

![](https://totvssuporte.zendesk.com/attachments/token/im7OgoBZu85lMcd87mirZHm7E/?name=inline-979524494.png)

**Ponto de Entrada/Filtro;**  
1. Realizar o acesso da rotina de Pedidos de Venda, com as customizações desabilitadas, e também verificar se no Dicionario, tem alguma chamada de customização. **Exemplo**: campo **C5\_TESTE**, esta chamando o **"U\_TESTE"**, retirar a chamada e verificar se ocorre o incidente;

**[MP - GPE - Como ativar e desativar customizações no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292)**  
2. Se o incidente ocorre somente com um Usuário, acessar a rotina Manutenção de Profile, no Configurador(SIGACFG), localizar o usuário e a rotina, e excluir o filtro que o usuário realizou e verifique se corrige o incidente;

**[MP - FRAME - Manutenção de Profile de Usuários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025097012-MP-FRAME-Manuten%C3%A7%C3%A3o-de-Profile-de-Usu%C3%A1rios?source=search)**

**Campo Customizado;**  
1. Campos customizados com informação de validação (X3\_RELACAO, X3\_INIBRW), com nome da coluna invalido;

**[MP - FAT - Erro Invalid column name(Nome de coluna inválido)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040569613-MP-FAT-Erro-Invalid-column-name-Nome-de-coluna-inv%C3%A1lido-?source=search)**

**Log de Inclusão(USERLGI )/Log de Alteração(USERLGA);**  
1. Verificar através do Configurador(SIGACFG), se existe em seu dicionário, os campos de Log **"USERLGA/USERLGA".**  
2. Verificar no **"X3\_INIBRW"** se esta com a função "EMBARALHA" caso esteja, o incidente esta ocorrendo devido essa função estar descontinuada pelo Protheus.  
3. Realizar a configuração desses campo de Log no Padrão através do Procedimento;

**[Rotinas de Logs e Auditoria](https://tdn.totvs.com/display/public/PROT/Rotinas+de+Logs+e+Auditoria)**

**Importante**: Para resolução de telas do Protheus que não estão adequadas, ajuste com o parâmetro **-DPI** no atalho do executável do SmartClient, conforme documentação da nossa equipe de Tecnologia: **[Parâmetros de linha - Smartclient](https://tdn.totvs.com/x/g49c)**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407433437591/mceclip0.png)**

***Lembrando que o suporte não orienta a rotinas customizadas, a orientação do suporte é sob dúvidas pontuais em ambiente padrão, conforme diretrizes de escopo do atendimento do suporte: [OINF0011 - Diretrizes de Atendimento Suporte Padrão](https://tdn.totvs.com/x/kO6nI)***

***Em caso de customizações de tela e outras rotinas valide a possibilidade da visita de um consultor in loco junto ao seu ESN - executivo de negócios da Totvs.***
