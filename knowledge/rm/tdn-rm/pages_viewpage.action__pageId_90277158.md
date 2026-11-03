---
content_hash: 347512c134f70a06b51ebf79b595a67a307dfbc3bc2c9e27f14576b0c5f509ea
fetched_at: '2026-06-29T00:12:02.702442+00:00'
page_id: '90277158'
product: rm
source: tdn-rm
title: Valor Monetário por Extenso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=90277158
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Gerador de Relatórios                         **Versão:** 11.52 |
| **Processo** | **:** | Impressão de Relatórios |
| **Subprocesso** | **:** | Valor Monetário por Extenso |
| **Data da publicação** | **:** | 04/11/2013 |

**Valor Monetário por Extenso**

        Em alguns relatórios, necessitamos imprimir o valor numérico de um determinado campo, por extenso. Dentre vários exemplos, podemos mencionar um relatório contratual que o valor do salário a ser contatado será impresso por extenso.

        No exemplo, utilizaremos um relatório com uma quebra por seção que em seguida listará as informações chapa, nome e salário por extenso de cada seção. Vejamos a estrutura do relatório e o resultado da sua impressão sem a devida configuração de impressão por extenso para o campo salário.

| Estrutura do Relatório |
| --- |
|  |
| Relatório Impresso |
|  |

        Mas como realizar a configuração no campo salário para que seu valor seja impresso como numérico? Primeiro selecione o componente salário, em seguida clique com o botão direito para que sejam listadas as opções de recursos deste componente. Dentre as opções selecione “Propriedades...”.

        O sistema carregará um mine formulário para parametrizações especiais. Neste formulário selecione a guia “Formatação”. Nas opções de “Categoria” selecione “Especial” para em seguida selecionar “Valor Monetário por Extenso”.

        Salve as configurações e em seguida gere o relatório novamente para validarmos as configurações.

| Relatório impresso com campo Salário por extenso |
| --- |
|  |

**Relatório com o salário impresso por extenso gerado com sucesso!**

---

**ATENÇÃO**

---

Em alguns casos se configura campos do relatório para serem impressos por extenso monetário, porém ao gerar o relatório a sua formatação **não é executada**. Deparando com esta situação acesse os parâmetros globais do sistema e na guia “Gerais” confirme se há preenchimento para o parâmetro **“Símbolo da Moeda”**. Atribua a simbologia **R$**. Salve as alterações, efetue Logout / Login e gere o relatório novamente.

**Observações:** Para acesso aos Parâmetros Globais através dos aplicativos em **Delphi** acesse; **“Opções | Parâmetros | Globais”**. Para acesso aos Parâmetros Globais através da nova **MDI** acesse; **“Ambiente | Configuração | Parâmetros | Globais”**.

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
