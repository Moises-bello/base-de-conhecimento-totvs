---
content_hash: d6660120b8672170b8d8b70f544be939e32e788e59cdc64a35233ca41a8359f3
fetched_at: '2026-06-29T00:12:01.349798+00:00'
page_id: '893433234'
product: rm
source: tdn-rm
title: Erro "certificado X.509"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=893433234
version: 3
---

Se encontrarem erros relacionados a certificados, especialmente nos portais, com mensagens como ***'certificado X.509'***, isso geralmente está associado a um certificado vencido no ambiente do cliente.

Identificamos que, no TCLOUD, em ambientes legados, o certificado foi atualizado apenas nas máquinas com portas publicadas. No entanto, não foi atualizado nas máquinas ***ELASTIC\_SERVICE e ELASTIC\_JOB***. Para corrigir esse problema, é necessário atualizar o certificado nessas máquinas, reiniciar o serviço do RM nelas e também o IIS nas máquinas de portais.

O certificado utilizado atualmente pela automação é válido até **06/08/2025.** No entanto, esse dado pode variar conforme o vencimento dos certificados futuros.

Erro:

**Aplicar permissão no certificado**

1. Acessar o executar e digitar: certlm.msc
   1. Ir em "Personal" > "Certificates";
   2. Clicar botão direito no certificado, selecionar a opção "Manage Private Keys";
   3. Adicionar a permissão de everyone;
   4. Caso já exista, não precisa adicionar;
   5. Reiniciar o Host e IIS dos Portais.
