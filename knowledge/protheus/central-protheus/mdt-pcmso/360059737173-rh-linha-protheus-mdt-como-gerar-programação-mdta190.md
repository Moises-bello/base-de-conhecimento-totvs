---
article_id: 360059737173
category: MDT - PCMSO
content_hash: bf526d0674f18a99adee2b0d38f7df378f7f9c59baed913137143dd19b2c3082
fetched_at: '2026-06-28T22:44:28.411523+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Como Gerar Programação (MDTA190)
type: support-article
updated_at: '2025-09-03T14:27:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059737173-RH-Linha-Protheus-MDT-Como-Gerar-Programa%C3%A7%C3%A3o-MDTA190
---

**Dúvida**Como gerar uma Programação de Exames rotina MDTA190?  
Como gerar o PCMSO (Programa de Controle Médico de Saúde Ocupacional)?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Para gerar Programação acesse o Módulo 35 (SIGAMDT), no caminho: **Atualizações > PCMSO > Gerar Programação.**

**1.** Na janela de **Gerar Programação**, selecione a opção **Incluir**.  
O Sistema apresenta a tela de inclusão.

**2.** Preencha os campos conforme orientação do help de campo.  
**3.** Confira os dados e confirme a inclusão.  
  
Exemplo de cadastro:  
  
![20201123_093633.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098121654)

A rotina **Gerar Programação** (*MDTA190*) tem como objetivo principal gerenciar e facilitar a geração da programação de exames dos funcionários de acordo com a faixa etária de cada um.   
A geração da programação de exames considera os exames relacionados ao **Programa de Saúde Func.** (MDTA115 - SIGAMDT), **Exames por Risco** (MDTA185 - SIGAMDT), **Exames por Função** (MDTA450 - SIGAMDT) e **Exames por Filial** (MDTA170 - SIGAMDT). É possível realizar a execução da rotina via ***Schedule.***A geração dos exames é realizada na opção de inclusão da rotina. Ao executar essa operação, o sistema analisa todos os funcionários registrados (na tabela *SRA*) que não tenham sido demitidos. Também é possível restringir a análise aos funcionários selecionados na opção **Ações Relacionadas / Funcionários.** Caso contrário, ao confirmar a operação, o sistema solicitará que o usuário escolha entre gerar os exames para **Todos os funcionários** ou para os **Selecionados.**Após a confirmação dos usuários que irão participar da geração da programação de exames, será verificado a opção selecionada no campo **Data Progr**. (*TMW\_BASEDT*), com isso poderá ter uma data de referência para o início do exame. Mas isso dependerá da opção selecionada, conforme:

**Data Programação de Exame**: Será utilizada a data do último exame programado, caso não houver, será pedido uma data.  
**Data Realização de Exame**: Será utilizada a data do último exame realizado, caso não houver, será pedido uma data.  
**Data do Ultimo Aso**: Será utilizada a data do último exame ASO realizado ou programado, caso não houver, será pedido uma data.  
**Data Aniversario**: Será utilizada a data de aniversário.  
**Data Admissão**: Será sempre utilizada a data de admissão, independentemente da existência de algum exame realizado pelo funcionário no mesmo período.  
**Data Informada**: Considera a data a informada no campo seguinte **Data Infor**. (*TMW\_DTREFE*).

Se a data de referência do exame não for informada, o conteúdo do campo Vencimento Exame Médico é verificado. Se o conteúdo estiver preenchido, a data de referência é gerada a partir desta data, se não estiver preenchido, a data de referência é gerada à partir da Data de Admissão. Isto ocorre quando o funcionário não possuir exames anteriores para referência.  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[MP - MDT - Como cadastrar Exames](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056538654)  
[MP - MDT - Como cadastrar Fornecedor de Exames](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056541274)  
[MP - MDT - Como cadastrar e definir os exames que serão apresentado no PCMSO (Programa de Controle Médico de Saúde Ocupacional)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059540413)  
[Gerar Programação](https://tdn.totvs.com/pages/viewpage.action?pageId=886640275)
