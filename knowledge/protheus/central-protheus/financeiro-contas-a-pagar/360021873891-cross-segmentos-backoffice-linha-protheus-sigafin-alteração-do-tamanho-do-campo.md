---
article_id: 360021873891
category: Financeiro - Contas a Pagar
content_hash: 887565548909f7c26481dbf46418bdf8bac9c24540d4a447b615ee6fef26cee5
fetched_at: '2026-06-28T22:38:07.048624+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Alteração do tamanho
  do campo Parcela
type: support-article
updated_at: '2026-06-19T15:19:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021873891-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Altera%C3%A7%C3%A3o-do-tamanho-do-campo-Parcela
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32550244992919) Tempo aproximado para leitura: 00:10 min**  
  
**Dúvida**  
Qual o procedimento para aumentar o tamanho do campo da parcela?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Para realizar essa alteração, siga os passos abaixo.

**Exemplo:** alteração do tamanho do campo **Parcela** de **1** para **3** caracteres.

1. Acesse o **Configurador**.

2. Navegue até **Ambiente > Cadastros > Parâmetros** e altere o parâmetro **MV\_1DUP** para **"AAA"** ou **"001"**. Esse parâmetro define a inicialização da primeira parcela do título gerado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41350462416407)

3. Em seguida, acesse **Base de Dados > Dicionário > Base de Dados**.

4. Clique em **Dicionário de Dados**, expanda **Grupo de Campos** e selecione **Descrição – Parcela**. Em seguida, clique em **Editar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41350450570135)

5. Na tela de edição da **Descrição – Parcela**, altere o **tamanho do campo** para **3** e salve a alteração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41350450570519)

6. Confirme a alteração e clique em **Atualizar Base de Dados** (ícone do disquete/engrenagem) para que o sistema altere o dicionário e as tabelas físicas;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41350450573463)

Ao realizar essa alteração, serão carregadas todas as tabelas que possuem vínculo com o campo **Parcela**, para que o ajuste do tamanho seja aplicado de forma consistente em todas elas.

**Importante**🚩️  
Além das alterações mencionadas, é necessário ajustar, via **RDMAKE**, o tamanho dos campos **E1\_TITPAI** e **E2\_TITPAI** para os registros já existentes na base de dados. Esse procedimento deve ser realizado conforme orientações descritas no boletim técnico abaixo, utilizando o exemplo de **RDMAKE** como referência.

O RDMAKE FinAjuTam.PRW está disponível para download no portal do cliente e no pacote abaixo:

[RDMAKE PADRÃO](https://suporte.totvs.com/portal/p/10098/download?e=1152102)

**O tamanho do campo** **Parcela** **deve ser alterado exclusivamente por meio do** **Grupo de Campos****, pois essa modificação impacta diversas tabelas do sistema e garante que o ajuste seja aplicado de forma consistente em todas.**

Não disponibilizamos documentação oficial para orientar a configuração ou customização em **RDMAKE**, pois esse tipo de implementação possui particularidades de acordo com o ambiente de cada empresa e, normalmente, é realizado por um analista especializado em atendimento **in loco**. Esse procedimento não faz parte do escopo de atendimento do **Help Desk**.

Da mesma forma, não realizamos análise ou validação de customizações do **RDMAKE ou base de dados**, uma vez que não temos acesso ao código-fonte dessas implementações e essa atividade também está fora do escopo do **suporte padrão**. Nesses casos, recomendamos que a avaliação seja realizada pelo desenvolvedor responsável pela customização e base de dados ou por um analista de  atendimento **in loco**.

**Saiba mais**

[FINA040 - Geração de desdobramento](https://tdn.totvs.com/pages/releaseview.action?pageId=306856119#:~:text=Essa%20op%C3%A7%C3%A3o%20permite%20a%20gera%C3%A7%C3%A3o,de%20alugu%C3%A9is%2C%20por%20exemplo).)

[Geração de Títulos por Desdobramento (FINA040 - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=306856119)
