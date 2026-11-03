---
article_id: 360016427572
category: Materiais - Compras (SIGACOM)
content_hash: 50db1fda428c441a7a3b95d49fbff5e0c574b249b97aec2d774bc1a3fd864d22
fetched_at: '2026-06-28T22:41:08.808473+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documentos de Entrada
  - Bloqueio de Movimentos
type: support-article
updated_at: '2025-11-27T18:23:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016427572-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documentos-de-Entrada-Bloqueio-de-Movimentos
---

**Dúvida**

Documentos de Entrada - Bloqueio de Movimentos

Como efetuar o lançamento de Documentos de Entrada (MATA103) e Nota Fiscal Eletrônica (SPEDNFE), a partir do módulo Compras, que permita inclusão de documentos bloqueados sem que haja movimentações nos módulos Livros Fiscais, Contábil, Financeiro e Estoque, independente da TES escolhida?

**Ambiente**

Protheus – Compras – A partir da versão 11.80

**Solução**  
**1**. Suponha que sua Empresa, situada no Sudeste do Brasil, compre mercadoria de um produtor Rural na Bahia. Conforme o regulamento de ICMS – BA, este produtor é dispensado de emitir Nota Fiscal.  
**2**. Para que a mercadoria entre no Estado de destino, deve existir um documento fiscal que regularize esta mercadoria. Assim, sua Empresa gera um documento de entrada com seu próprio formulário, para que este documento acompanhe a mercadoria no momento em que entrar no seu Estado, até a chegada na empresa.  
**3**. Com o processo descrito acima, a Empresa do Sudeste precisa escriturar os Livros Fiscais, gerar o Estoque e lançar os títulos somente quando a mercadoria chegar. Além do mais, por ser uma empresa obrigada a transmissão da Nota Fiscal Eletrônica, precisa realizar a transmissão da nota no momento que a mesma foi emitida e logo após imprimir o DANFE.  
**4**. O tratamento possibilita a inclusão de um documento de entrada com formulário próprio, bloqueando as movimentações de Livros, Estoque e Financeiro. Permite a transmissão e impressão do DANFE, para que na chegada da mercadoria a nota receba classificação e gere movimentações de Livros, Estoque e Financeiro.

***Procedimentos de Utilização:***  
**1.** No módulo Compras, clique na opção "Atualizações/Movimentos/Documento Entrada".

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060411394)

**2.** Pressione a tecla F12 em seu teclado, ao visualizar o browser da rotina. O Sistema exibirá uma tela de configuração de parâmetros que contém as perguntas da rotina. Localize a pergunta "Bloq. Movimento" e selecione “Sim”. Confirme no botão “Ok”.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060411494)

**3.** De volta no browser, clique no botão "Incluir".

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061336793)

**4.** Realize o lançamento do Documento de Entrada. No campo "Form. Próp" (Formulário Próprio) selecione a opção "Sim" e em "Espec.Docum." (Espécie de Documento), selecione "SPED". Certifique-se da movimentação e confirme. A nota aparecerá com um marcador de cor violeta. Consulte o botão "Legenda" no browser.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060411734)  
  
Neste exemplo, o status da nota deve ser "Documento Com Bloqueio de Movimento" e, portanto, não gerou movimentações de Livros, Estoque e Financeiro.  
Se o contribuinte está obrigado à transmissão da NF-e, é possível transmitir normalmente a nota bloqueada. Para isso, acesse a rotina da NF-e. Mais detalhes sobre este procedimento devem ser consultados no boletim "NF-e Sefaz".

**5**. Para o desbloqueio da nota e geração dos registros nos Livros Fiscais, Estoque e Financeiro será necessário classificá-la. Acesse o módulo Compras, opção "Atualizações /Movimentos / Documento Entrada".  Pressione a tecla F12 em seu teclado, ao visualizar o browser da rotina. selecione a opção "Não".

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061337093)

**6.** Posicione o cursor do mouse sobre a nota bloqueada e pressione o botão "Classificar".

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061337073)  
  
No momento da classificação, para as notas transmitidas, não será possível realizar alterações no item e no cabeçalho, assim como nas abas Impostos, Descontos/Fretes/Despesas e Livros Fiscais. Após visualizar o documento na classificação, confirme no botão "OK".

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060412254)

**7.** Neste momento, serão geradas todas as movimentações e o documento será desbloqueado. Para constatar, verifique o marcador ao lado do número do documento ou clique no botão "Legenda", localizado no browser.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061337373)

***Obs:***  
Esta implementação foi realizada com exclusividade no processo em que o documento de entrada tem origem pelo módulo de Compras. Em documentos manuais de entrada (Livros Fiscais), este tratamento não está disponível.

***Importante:***  
Para evitar inserir desnecessariamente a condição do bloqueio para todas as próximas notas, por vezes com outras características, desabilite a opção "Sim" na pergunta "Bloq. Movimento" assim que finalizar a inclusão do documento bloqueado.

***Obs 1 :***

Esta funcionalidade não realiza o bloqueio a partir de um intervalo de data ou de numeração de NFs, mas sim apenas ativando e desativando o parâmetro F12, conforme orientado nas instruções acima.

***Obs 2 :***

Pelo padrão do sistema, é possível se excluir uma nota de entrada, com bloqueio de movimentos ( legenda roxa ), visto que a não foi classificada efetivamente ainda, ou seja, não foram efetuadas as integrações com os demais módulos de acordo com o TES utilizado inicialmente.

Caso seja necessário a não permissão da exclusão, temos 2 pontos de entrada que podem ser testados e verificados :

**A103VLEX** - Determina validações adicionais na exclusão do documento de entrada  
Link:<https://tdn.totvs.com/x/Vtxc>

**MT103EXC** - Valida exclusão do documento de entrada  
Link:<https://tdn.totvs.com/x/kYsDCw>

***Obs 3:***

Caso a Nota esteja Bloqueada e já tenha sido transmitda para a Sefaz , não será permitido a exclusão, e será apresentado o Help abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26999597867159)

Só será permitido a exclusão após a Classificação da nota.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
