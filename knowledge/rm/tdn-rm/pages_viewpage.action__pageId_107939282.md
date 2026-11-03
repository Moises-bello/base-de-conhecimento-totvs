---
content_hash: 3b51727002dfea5f8d0963467bb57e5c75a9edf6cb8c9b5ccf2cedb38a6a664d
fetched_at: '2026-06-29T00:05:54.390685+00:00'
page_id: '107939282'
product: rm
source: tdn-rm
title: Utilizando campos Auto Incremento no novo conceito.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=107939282
version: 11
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Integração                    **Versão:**11.82 |
| **Processo** | **:** | Conceito |
| **Subprocesso** | **:** | Como utilizar campos Auto Incremento no novo conceito |
| **Data da publicação** | **:** | 19/12/2013 |

Ao criar um conceito que utilize chave primaria em sua estrutura temos que ter atenção ao associar um campo à esta chave. Caso exista algum registro na estrutura de origem, onde a chave primária seja igual à chave do registro de destino, quando executado, o mesmo retornará que o registro não poderá ser inserido, pois a chave já existe.

Utilizando a operação de “Auto Incremento” sempre que um registro for migrado ele terá uma chave única.

**Como utilizar o campo Auto Incremento.**

Primeiramente precisaremos criar a operação de Auto Incremento.

Acesse o menu operações na estrutura do novo conceito.

Clique em adicionar e selecione a opção **"Auto-incremento (RM)"**.

Após clicar em **"Auto-incremento (RM)"** será exibida a operação para ser preenchida.

|  |
| --- |
| Preencha o campo **"Nome"**. |
| Selecione sua estrutura de destino no campo **"Conexão"**. |
| No campo **"Cód.AutoInc"** pode-se utilizar registros já existentes, provenientes da **tabela "GAUTOINC"** e novos registros, onde serão inseridos na tabela "GAUTOINC" com o mesmo nome preenchido no campo "Còd.AutoInc". No exemplo foi utilizado o **"IDPATRIMONIO"**. |

Após criar a operação é preciso associa-la ao campo de destino. Para associar arraste a operação ao campo de destino desejado.

No exemplo utilizado o campo de destino escolhido foi o IDPATRIMONIO. Após a associação serão criados dois novos campos "Coligada" e "Sistema". Estes campos definirão a partir de qual registro da tabela "GAUTOINC" será gerado o seu IDPATRIMONIO.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
