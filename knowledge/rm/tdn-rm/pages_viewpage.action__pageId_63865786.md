---
content_hash: c6a657f2cced5d41f87048b586667c77a7d892d14ed5aa14f023dc10008e668b
fetched_at: '2026-06-29T00:11:07.007152+00:00'
page_id: '63865786'
product: rm
source: tdn-rm
title: Apuração do ISS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=63865786
version: 17
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.52 |
| **Processo** | **:** | Check List Apuração de ISS |
| **Subprocesso** | **:** | Parametrizar o sistema para apurar o tributo ISS |
| **Data da publicação** | **:** | 28/06/2013 |

**Definição do Processo**

---

Este “Como Fazer” tem por objetivo auxiliar o usuário na parametrização do sistema RM LIBER para correta apuração do tributo “ISS (Imposto Sobre Serviço)”, será verificado desde os cadastros do Imposto até a geração da guia de recolhimento no período de apuração.

 

**Parametrizações Necessárias**

---

**1. Cadastro do tributo**

 O ISS é o único tributo que o sistema consiste a sigla cadastrada no tributo, sempre deve ser  ISS, nunca cadastre ISS 1 ou ISS 2 ou etc:

**2. Verificação do Lançamento Fiscal**

As notas de prestação de serviço devem ter o tributo com a sigla “ISS” informado no lançamento fiscal com tipo de recolhimento selecionado, base do tributo, alíquota e valor do tributo se houver destaque do tributo.

***Importante: “Tributo no Item ou no Lançamento?”***

Caso a opção "Utiliza Município de Prestação de Serviço por Item de Lançamento" esteja marcada em Opções | Parâmetros | Gerais Tabelas | Identificação de Regras de Apuração | ISS | Regras ISS por Filial | Editar a Filial | Const. Civil e Deduções,**o sistema irá considerar o tributo informado****na aba Outros Tributos do “item” do lançamento fiscal**, observando que o município é a codificação do serviço deverão estar informadas na aba Outros Dados sub- aba Prestação de Serviço também do “item”.

**3. Data de Apuração do Tributo**

Data de Apuração do ISS deve ser parametrizada no menu abaixo:

* Opções | Parâmetros | Gerais Tabelas | Apuração de Tributos | ISS | Apuração de ISS por Filial | Editar a Filial | Data de Apuração do ISS.

**Os parâmetros são:**

* **Lançamento de Entrada**- Corresponde à data a ser utilizada para seleção de Lançamentos de Entrada;
* **Lançamento de Saída**– Entidade Privada - Corresponde à data a ser utilizada para seleção de Lançamentos de Saída – Participante entidade privada;

**Lançamento de Saída**– Entidade Pública -Corresponde à data a ser utilizada para seleção de Lançamentos de Saída – Participante entidade pública;

Cada um desses parâmetros poderá receber qualquer dos três valores determinados abaixo:

**Data de Emissão**

**Data de Entrada/Saída**

**Data de Pagamento/Vencimento**

**Importante:**Caso seja selecionada a terceira opção (Data de Pagamento/Vencimento) o sistema se comportará da seguinte forma:

* Se existir integração com o Financeiro (RM Fluxus), serão selecionados os lançamentos Fiscais de acordo com a Data de Baixa do Lançamento Financeiro vinculado, entrando na seleção somente os Lançamentos Fiscais cujo Lançamento Financeiro associado esteja baixado e será considerada a data da primeira baixa;
* Se não existir integração com o Financeiro, serão selecionados os Lançamentos Fiscais de acordo com a Data de Vencimento, existente na aba “Dados Financeiros” do Lançamento Fiscal.

**4. Cadastro Filial**

Opção “Filial Responsável pela Retenção” esta marcada, acesse Cadastro | Filial | Anexos | Dados Fiscais | Aba Tributos.

***5. Cadastro Cli/For***

***Marcar a opção “Contribuinte ISS” acesse Cadastro | Cli/For | Dados Fiscais | sub aba Classificação.***

***6. Cadastro Natureza Fiscal***

***Demarcar a opção “Natureza Fiscal” no cadastro da natureza selecionada no lançamento fiscal***

* ***Novo modelo BackOffice***

Acesse Cadastro | Natureza de Operação | Cadastro de Natureza de Operação | Identificação da Natureza Fiscal

* ***Antigo modelo***

Acesse Cadastro | Natureza de Operação | Cadastro de Natureza de Operação | Aba Outros Dados

***7. Cadastro Produto***

Produto do tipo “Serviço” acesse Cadastro | Produto 

***Guia de Recolhimento:***

*Depois basta ir em processos e clicar em  “Geração de Guias Automaticamente”:*

***8. Geração da Guia***

No período de apuração do ISS na aba outros dados serão informados os valores a recolher do tributo (Débito ou Crédito)

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ApuracaoISS.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
