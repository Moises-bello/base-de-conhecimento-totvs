---
article_id: 39607401174167
category: RH - Folha de Pagamento
content_hash: 5975b09f3dfe556288b45217909acf095a19055b4423ecb9c4e8f51aef409269
fetched_at: '2026-06-28T22:44:12.221738+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular adicional de cargo/função
type: support-article
updated_at: '2026-04-08T18:49:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39607401174167-RH-Linha-Protheus-GPE-Como-calcular-adicional-de-cargo-fun%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39607401120279) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como calcular adicional de cargo/função?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

A configuração dos adicionais poderá ser realizada no cadastro de funções, em uma nova aba, onde poderão ser definidos adicionais por percentual e/ou valor fixo, calculados com base no salário do funcionário, salário mais verbas, piso do sindicato, salário mínimo e salário mínimo estadual.

Na imagem a seguir pode ser visto a aparência do novo cadastro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39608844861591)

**Importante:** Não pode ser cadastrado mais de um adicional do mesmo tipo de adicional, tipo de cálculo e base de cálculo. Na hipótese de ter mais de um adicional com as mesmas configurações para uma função, deverá ser criado um novo tipo de adicional na tabela SX5 (UX).

Também não será permitido o cadastro da mesma verba de pagamento em mais de uma linha para o mesmo roteiro, sendo necessário definir uma verba para cada adicional.

A nova tabela RUJ deverá ter o mesmo compartilhamento da tabela SRJ.

Para que o cálculo seja efetuado foi incluído uma nova fórmula **S\_CADIFUNC**, que foi adicionada nos roteiros de cálculo específicos.

A fórmula foi incluída antes do cálculo dos adicionais de periculosidade/insalubridade e ATS por verbas. Caso efetue estes cálculos por salário mais verbas e tenha a intenção que eles componham a base do adicional por função, a fórmula deverá ser reposicionada no roteiro para ser executada após as fórmulas dos adicionais por verbas.  
  
**Obs.:** Não temos um identificador de cálculo especifico para o adicional. O sistema irá observar o Salário do cadastro do funcionário para realização  do cálculo.

**Saiba Mais**  
[Cálculo Adicional por função](https://tdn.totvs.com/pages/viewpage.action?pageId=799276835)  
[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
