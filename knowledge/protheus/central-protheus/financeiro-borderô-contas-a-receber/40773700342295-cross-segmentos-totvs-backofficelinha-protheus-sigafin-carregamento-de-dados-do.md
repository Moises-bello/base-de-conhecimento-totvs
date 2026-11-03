---
article_id: 40773700342295
category: Financeiro - Borderô contas a Receber
content_hash: d8b515b7b344fdcbe87146efa7cee0002946bd4984d8464e806deb7645e6e786
fetched_at: '2026-06-28T22:37:39.749046+00:00'
product: protheus
section_id: 35057237655191
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice(Linha Protheus) - SIGAFIN - Carregamento
  de dados do banco na criação de borderô
type: support-article
updated_at: '2026-06-26T13:13:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40773700342295-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Carregamento-de-dados-do-banco-na-cria%C3%A7%C3%A3o-de-border%C3%B4
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40773700324119)** Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Ao realizar a seleção do banco durante a criação do borderô, o sistema está carregando os dados de forma incorreta ou alterando a conta selecionada.

**Ambiente**  
Cross Segmento - Linha Protheus - SIGAFIN - Release 12.1.2410 e superiores **(Após expedição contínua de Junho/2026)**  
  
**Solução**

Esse comportamento ocorre devido a uma atualização de usabilidade implementada no sistema.

A partir da expedição contínua de Junho de 2026, com o objetivo de otimizar a experiência de utilização nas rotinas **FINA060** e **FINA061**, ao utilizar a opção **“Borderô”** e preencher o campo **“Banco”**, o sistema passa a carregar automaticamente o primeiro registro ativo correspondente ao banco informado.

Caso o primeiro registro localizado para o banco selecionado esteja configurado como bloqueado, o sistema irá desconsiderar esse registro e assumirá automaticamente a próxima conta ativa disponível para utilização.

O preenchimento automático poderá ocorrer de duas formas, conforme a ação realizada pelo usuário:

1. **Comportamento via preenchimento manual:** Ao introduzir o código do banco manualmente (em que a primeira conta associada está bloqueada), o sistema carregará de forma automática o primeiro registo de conta ativo que estiver disponível para utilização.
2. **Comportamento via consulta F3:** Na seleção através da consulta padrão F3, o registo bloqueado será inicialmente apresentado na lista de pesquisa. No entanto, após confirmar a escolha, o sistema carregará automaticamente o registo ativo subsequente que estiver disponível para utilização.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/41229006271255)](https://centraldeatendimento.totvs.com/hc/article_attachments/41229006271255)

**Observação Importante**:

Veja que na imagem o <F3> (clique na lupa) é apresentado o banco bloqueado 1

Esse comportamento é esperado no padrão atual do produto e foi implementado para evitar a utilização de contas bancárias bloqueadas durante o processo de geração do borderô.

|  |
| --- |
| Cenário com compartilhamento SA6 e SEE diferentes, sem bloqueio no cadastro de banco, porém auto preenchendo (gatilhando) a agencia e conta de outra filial diferente que estou logado no momento de digitar o banco e pressionar <TAB> no teclado, qual o motivo? |

Caso tenha a :

SE1 Contas a receber ,SEA Borderô , SEE parâmetros de bancos,  com compartilhamento = Exclusivo

SA6 Cadastro de banco = Compartilhado

No cadastro de banco MATA070 (tabela SA6 - Compartilhada) tenha

|  |  |  |  |
| --- | --- | --- | --- |
| filial | banco | agencia | conta |
|  | 001 | 1607 | 001697 |
|  | 001 | 0001 | 000123 |

No cadastro de parâmetros de  banco FINA130 (tabela SEE - Exclusiva) tenha

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| filial | banco | agencia | conta | sub-conta |
| 01 | 001 | 0001 | 000123 | 0 |
| 02 | 001 | 1607 | 001697 | 0 |

Logado na filial 02 

Na rotina "FINA060 - Borderô e Recebimentos" ao preencher somente o código do banco 001 dentro do campo CPORT060, e clicar no botão <TAB>  do teclado

Automaticamente irá auto preencher (gatilhando) nos campos os seguintes conteúdos:  
CAGEN060 = 0001

CCONTA060 = 000123

Qual o motivo da rotina FINA060 de ter preenchido o banco, agência e conta com dados bancários da filial 01 e não da filial 02 que estou logado?

Porque o cadastro que o sistema obtém as informações para trazer em tela são do cadastro de banco MATA070  da tabela SA6 e não da tabela SEE - Parâmetros de banco FINA130. E ao clicar na lupa do campo CPORT060 e tentar incluir uma informação, será a tela de cadastro de bancos, e não do parâmetros de banco.

Saiba Mais:

[Borderô de Recebimento com Impostos - FINA061 - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=95617838)

[Transferências - FINA060 - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=271405699)
