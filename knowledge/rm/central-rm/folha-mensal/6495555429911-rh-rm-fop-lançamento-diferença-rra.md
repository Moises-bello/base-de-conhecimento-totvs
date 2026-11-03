---
article_id: 6495555429911
category: Folha Mensal
content_hash: d8959f22820e3d35eb788da8dafba5794309d38632766a94adf1bb92f057517a
fetched_at: '2026-06-28T22:46:59.167899+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Lançamento Diferença RRA
type: support-article
updated_at: '2025-01-21T17:52:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6495555429911-RH-RM-FOP-Lan%C3%A7amento-Diferen%C3%A7a-RRA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura **00:04:00 min  
  
Dúvida**Como é realizado o processo para cálculo e lançamento de RRA?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de pagamento - Todas as versões  
  
**Solução**No TOTVS Folha de Pagamento, para gerar as informações dos funcionários que receberam este tipo de verba, existem dois processos:

* **Parametrização via Histórico de RRA - INSERIDO MANUALMENTE**

Caso as verbas sejam **oriundos das decisões das Justiças do Trabalho, Federal, Estaduais e do Distrito Federal**, deverá cadastrar o Histórico de RRA, que está localizado no cadastro dos Funcionários.

* No cadastro de funcionários, o histórico estará disponível no menu **Anexos I Históricos I Histórico RRA**

Exemplo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011675702/mceclip1.png)  
  
- Os campos referentes a **Dados do Advogado(a)** e **Nro Processo** passam a ser obrigatórios;

- Deverão ser incluídos históricos específicos, para cada processo de um mesmo funcionário;

- Deverão ser incluídos históricos específicos, para cada dependente o valor da Pensão Alimentícia.

* **Parametrização Via Cálculo / Lançamento de Diferenças**

Caso as verbas sejam **provenientes do trabalho**, não por processo judicial, deverá ser lançado no envelope os eventos provenientes de diferença salarial por dissidio, com os códigos de cálculo específicos para RRA.

Para realizar o processo corretamente, execute os seguintes passos:

1. Acesse o menu **Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Geral** e marque a flag **Utiliza Cálculo de RRA****![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011961801/mceclip6.png)**2. Cadastre todos os códigos de calculo específicos para RRA conforme tabela abaixo:

[Código de Cálculo 204 – Base IRRF RRA](https://tdn.totvs.com/pages/viewpage.action?pageId=452719730)

[Código de Cálculo 205 – INSS Descontado RRA](https://tdn.totvs.com/pages/viewpage.action?pageId=452718220)

[Código de Cálculo 206 – Pensão Alimentícia Judicial RRA](https://tdn.totvs.com/pages/viewpage.action?pageId=452718806)

[Código de Cálculo 207 – IRRF RRA](https://tdn.totvs.com/pages/viewpage.action?pageId=452718702)

[Código de Cálculo 208 - Base IRRF RRA Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452719848)

[Código de Cálculo 209 - INSS Descontado RRA Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452719900)

[Código de Cálculo 210 - Pensão Alimentícia Judicial RRA Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452719895)

[Código de Cálculo 211 - IRRF RRA Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452719935)

[Código de Cálculo 212 - Base IRRF RRA 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719669)

[Código de Cálculo 213 - INSS Descontado RRA 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719681)

[Código de Cálculo 214 - Pensão Alimentícia Judicial RRA 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719621)

[Código de Cálculo 215 - IRRF RRA 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719921)

[Código de Cálculo 216 – Mês RRA](https://tdn.totvs.com/pages/viewpage.action?pageId=452718723)

[Código de Cálculo 217 - Mês RRA Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718721)

[Código de Cálculo 218 - Mês RRA 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452718722)

3. Para que o sistema tenha referência para cálculo dos valores, cadastre a tabela de cálculo IRRF de RRA no menu **Administração de Pessoal I Cálculos I Tabelas de cálculos**  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011954461/mceclip5.png)

* Deverá cadastrar tabela de IRRF de RRA com vigência no ano referência dos eventos, se o pagamento das diferenças for em janeiro 2021 retroativo a 12/2020, irá cadastrar a tabela de 2020;
* Deverá cadastrar as faixas de calculo IRRF de RRA com os valores específicos, para o cálculo correto do desconto;
* Deverão ser incluídos históricos específicos, para cada dependente o valor da Pensão Alimentícia.

4. Depois de realizar a alteração salarial poderá executar a rotina de diferença salarial:

[RH - RM - FOP - Diferença salarial por dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008178291-RH-RM-FOP-Diferen%C3%A7a-salarial-por-diss%C3%ADdio)  
  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011967641/mceclip7.png)

5**.** No envelope do funcionário, serão lançados os eventos de base para RRA:  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011696562/mceclip8.png)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011698022/mceclip9.png)  
  
**Saiba Mais**

[RH - RM - FOP - Diferença salarial por dissídio retroativa à competência atual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414433322519-RH-RM-FOP-Diferen%C3%A7a-salarial-por-diss%C3%ADdio-retroativa-%C3%A0-compet%C3%AAncia-atual)
