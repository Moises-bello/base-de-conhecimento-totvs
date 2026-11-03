---
article_id: 360055929414
category: Financeiro - Conciliação de Vendas
content_hash: cfdb06dde76b72acc27fa147a7f818e206fc8fc07a57ea4044e66bdcc41463f2
fetched_at: '2026-06-28T22:37:26.258178+00:00'
product: protheus
section_id: 35058743504791
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus  - FINA914 - Como selecionar opção
  de layout
type: support-article
updated_at: '2026-02-11T16:57:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055929414-Cross-Segmentos-Backoffice-Linha-Protheus-FINA914-Como-selecionar-op%C3%A7%C3%A3o-de-layout
---

**Dúvida**  
Como selecionar opção de *layout?*  
  
**Ambiente**  
Cross Segmentos - Backoffice Linha Protheus - FINA914 - A partir da versão 12.1.27.  
  
**Solução**  
Para acessar os *layouts*, crie primeiramente os diretórios, a seguir cadastre os diretórios no Módulo Loja, rotina **LOJA075 Código de Administradores SITEF.**  
  
Conforme a documentação oficial, veja as premissas:  
[Conciliador Pagamentos e Vendas](https://tdn.totvs.com/display/public/PROT/Conciliador+Pagamentos+e+Vendas+-+Financeiro+%28Contas+a+Receber%29+-+P12)  
  
![](https://totvssuporte.zendesk.com/attachments/token/Dw8F3eU4SKokKJ7RrzbRNqDEq/?name=inline1884070475.png)​

**Importante:**  
Para gravação no **protheus\_data**, não será necessário colocar o diretório, somente as barras conforme tela acima, ou se preferir pode ser criado um subdiretório específico, porém, precisará colocar o caminho correto. **Exemplo**: C:\BASELINE\CARTAO\AMEX\IMPORT

Após cadastrar o diretório, na pasta **Import,** colocar o arquivo do **TEF**, desta maneira conseguirá habilitá-lo.
