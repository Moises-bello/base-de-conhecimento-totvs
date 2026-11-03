---
content_hash: 2eb4e03d4cff6e71433913bf57e5e3629adabeba94dd3a2e006f6909f71c1555
fetched_at: '2026-06-29T00:11:12.252125+00:00'
page_id: '65208641'
product: rm
source: tdn-rm
title: Como Criar Totalizador com Quebra por Grupo
type: documentation
url: https://tdn.totvs.com/display/LRM/Como+Criar+Totalizador+com+Quebra+por+Grupo
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.82 |
| **Processo** | **:** | Report |
| **Subprocesso** | **:** | Como Criar Totalizador com Quebra por Grupo |
| **Data da publicação** | **:** | 04/07/2013 |

Em nosso exemplo, temos as seguintes informações no relatório:

1. Grupo de Seção (PSECAO)
2. Grupo de Funcionário (PFUNC)

Vamos elaborar um relatório onde será gerada a Seção dos funcionários e seus respectivos funcionários, porém quebrando / organizado por secção. Ao final de cada seção, vamos totalizar o salário dos funcionários por seção.

ESTRUTURA INICIAL DO RELATÓRIO

Para iniciar a configuração de totalização por seção, crie um cabeçalho de detalhe 01.

Após criar o grupo CabeçalhoDeDetalhe1, clique na “setinha” do grupo. Abrirá uma janela de funções desde grupo.  Logo após, clique na função de Ordenação / Quebra (...)

Após abrir o GrouoField Collection Editor, clique em Add para inserir o campo que será sua referência da quebra. No nosso exemplo, vamos quebrar pelo código da seção (Psecao.codigo)

 

Do mesmo modo, crie um cabeçalho de detalhe para o detalhe 2 (Funcionário). Nesta etapa, não precisará efetuar configurações de quebra, apenas a inclusão do cabeçalho.

Para finalizar, selecione o campo totalizador localizado no Rodapé de Detalhe 1, clique em sua “setinha” para exibir suas funções. Marque a opção Zerar na Quebra.

Com isso, sempre que o Report finalizar a geração da Seção, ele efetuará a totalização de salário dessa seção. Ao iniciar uma nova seção, o totalizador será zerado buscando os novos valores.

**Relatório para DOWNLOAD:**

**Relatório para DOWNLOAD: Exemplo de relatório por sentença sql:**

|  |  |
| --- | --- |
|  | **Para maiores informações:**  Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha). |
