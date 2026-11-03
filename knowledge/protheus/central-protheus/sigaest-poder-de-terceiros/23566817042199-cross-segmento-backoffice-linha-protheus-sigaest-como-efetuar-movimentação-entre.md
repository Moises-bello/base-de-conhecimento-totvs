---
article_id: 23566817042199
category: SIGAEST - PODER DE TERCEIROS
content_hash: 5c74f2bd9e09bbd5c08af059744a1998e090c95b74018abb62cc2291a33a8b62
fetched_at: '2026-06-28T22:39:03.145293+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como efetuar movimentação
  entre Armazéns de endereços diferentes, para uma mesma filial
type: support-article
updated_at: '2025-03-12T12:26:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23566817042199-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-movimenta%C3%A7%C3%A3o-entre-Armaz%C3%A9ns-de-endere%C3%A7os-diferentes-para-uma-mesma-filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23566817009815) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**

Possuo um ou mais armazéns de uma Filial, em endereços diferentes, e tenho a necessidade de gerar uma nota para o transporte da mercadoria, sem alimentar o controle de Poder de Terceiro.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Solução**

Após avaliação do [embasamento legal avaliado pelo nosso time de Consultoria de segmentos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=625177351) segue recomendação de como realizar o procedmento:

---

**Passo a passo para o processo:**

1. **Criar o armazém no Protheus:** Não há regras especiais para a criação desse armazém.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/28792023370007)
2. **Criar um cliente:** Use o CNPJ da filial proprietária do armazém e cadastre os mesmos dados da filial.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/28792040084119)
3. **Criar um fornecedor:** Use o CNPJ da filial proprietária do armazém e cadastre os mesmos dados da filial.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/28792023377047)  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/28792023379223)  
   (Obs: CNPJ's e dados utilizados, foram gerados de maneira aleatória, apenas para exemplo)
4. **Cadastrar TES de entrada e saída:** Configurar para que não seja movimentado estoque (F4\_ESTOQUE = Não). As TES serão usadas para gerar as notas fiscais.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/28792023381655)
5. **Transferência entre armazéns:** Realize normalmente via Protheus.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/28792040089879)
6. **Gerar a nota de saída:** Use a rotina MATA920, com o cliente e TES criados no passo 4. A quantidade e o produto devem ser os mesmos do passo 5.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/28792040090647)
7. **Gerar a nota de entrada:** Use a rotina MATA910, com o fornecedor e TES criados no passo 4. A quantidade e o produto devem ser os mesmos do passo 5.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/28792023385751)

**Observação:** O Passo 5 controla o estoque no sistema, enquanto os Passos 6 e 7 geram as notas fiscais necessárias para o transporte da mercadoria. Consulte sua equipe fiscal para verificar eventuais necessidades fiscais adicionais.

**Importante:** Este procedimento consiste em proporcionar as movimentações sistêmicas para atender à legislação. Caso deseje que este processo ocorra de forma automatizada, é possivel seguir algumas alternativas: <https://tdn.totvs.com/x/R1gjIw>

---

**Complementar:**

Consulte também movimentações atendidas pelo controle de poder de/em Terceiro no Protheus: [Poder DE/EM Terceiro](https://tdn.totvs.com/pages/viewpage.action?pageId=446701767)

Consulte também como realizar o procedimento quando o armazenamento é realizado em espaço de Terceiros: [SIGAFAT (Faturamento) - Remessa/Devolução de Armazenamento no Faturamento (Poder De/Em Terceiro)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11272173598359-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Remessa-Devolu%C3%A7%C3%A3o-de-Armazenamento-no-Faturamento-Poder-De-Em-Terceiro)

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)
