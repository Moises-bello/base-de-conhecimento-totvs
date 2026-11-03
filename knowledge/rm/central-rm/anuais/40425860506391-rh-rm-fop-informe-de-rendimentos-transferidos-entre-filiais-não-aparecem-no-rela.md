---
article_id: 40425860506391
category: Anuais
content_hash: 7c08e612d58c536d1dcd7282200cc05db088c74e2e655d7f6709176cedc4ac78
fetched_at: '2026-06-28T22:46:50.937400+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP -  Informe de Rendimentos: Transferidos entre Filiais não aparecem
  no relatório'
type: support-article
updated_at: '2026-05-25T18:15:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40425860506391-RH-RM-FOP-Informe-de-Rendimentos-Transferidos-entre-Filiais-n%C3%A3o-aparecem-no-relat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40425919974295) Tempo aproximado para leitura: **00:05:40 min**  
  
**Dúvida**  
Como realizar a conferência de transferidos que não são levados para um único relatório de informe de rendimentos ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
  
Para conferência é necessário validar alguns pontos conforme demonstrado abaixo:

* **Validação do Tipo de transferência:**

Primeiramente verifique como ocorreu a transferência se foi uma transferência entre filiais ou coliga. Funcionários que foram transferidos entre filiais (ou seja, dentro da mesma coligada), quando gerar o informe de rendimentos o relatório não irá apresentar as informações das chapas de origem e de destino, é preciso realizar a validação conforme o exemplo abaixo:

*Funcionário FERNANDO*

*chapa 00006*

*Seção: 01.05 -  CNPJ XX.XXX.XXX/000X-XX.*

No mês 11/2024 teve transferência entre filial para seção 02.01 CNPJ XX.XXX.XXX/000Y-YY o mesmo da filial anterior só alterando os dígitos finais.

**Observação:** Por se tratar da mesma coligada, essa transferência é realizada pelo processo de rescisão **Folha mensal | Rescisão| tipo por transferência.**

Cadastro do funcionário ficou da seguinte forma:   
  
Chapa 00006 - Ativo na FILIAL 02 seção 02.1  
Chapa 12052 - Demitido na FILIAL 01 seção 01.05

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40724184026263)

* **Conferência do Histórico de Transferência:**

Próxima informação a ser verificada é, preenchimento do histórico de transferência, preenchido automaticamente no processo de rescisão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40425860483735)

* **Conferência no Cadastro do funcionário:**

Verificar o campo **data de transferência** localizado em **Administração de pessoal | Funcionários | aba Registro | sub aba Dados do Registro**

**Importante:** Esta verificação deve ser feita no cadastro da chapa ativa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40724154989591)

* **Conferência da geração do Informe de rendimentos:**

Para consolidar as informações das filiais origem e destino em um único informe de rendimentos, configure corretamente a quebra da empresa. Acesse **Anuais |  Dirf/Informe de rendimentos** ,  na grade seleção do campo **Quebra de Seção**, selecione a quebra empresa com a quantidade de dígitos da Matriz, no exemplo é zero ou seja uma única interrogação na quebra (**?).**  
  
**Importante:** para funcionários que tiveram transferência entre filiais é gerado apenas um relatório.  
Além disso,  para consultar a estrutura de seção acesse A**dministração de pessoal | Seções.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40425860486167)

Verificar também o campo **Quebra de seção** localizado nos parâmetros específicos da coligada, durante a geração do Informe de rendimentos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40724154992279)

Ao gerar o relatório com a configuração acima, serão consideradas as  informações da pessoa ( mesmo CPF) para um único relatório, lembrando que se tratar de coligadas diferentes ou seja CNPJS completamente destintos. Portanto, é necessário a geração de um informe de rendimentos por cada coligada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40724184031383)

**Importante:** Orientamos utilizar o  **Log da DIRF** para conferência e  verificar as movimentações da chapa origem e destino.

**Saiba mais:**

[RH - RM - FOP - Como gerar o Log da DIRF conferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38575728647447-RH-RM-FOP-Como-gerar-o-Log-da-DIRF-confer%C3%AAncia)

[RH - RM - FOP - DIRF/Informe de Rendimentos: Emissão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021081532-RH-RM-FOP-DIRF-Informe-de-Rendimentos-Emiss%C3%A3o)
