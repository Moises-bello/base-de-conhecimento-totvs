---
article_id: 13807332750231
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: b8dec66b82163958616e88209fdca8672916b8d159e36f79ef8d4997e9304ffb
fetched_at: '2026-06-28T22:47:29.481808+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Como aumentar a segurança do Meu RH
type: support-article
updated_at: '2025-12-26T17:21:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13807332750231-RH-RM-Meu-RH-Como-aumentar-a-seguran%C3%A7a-do-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23768490707095) Tempo aproximado para leitura: **00:03:47 min**  
  
**Dúvida**  
Como aumentar o nível de segurança do aplicativo Meu RH e criptografia dos dados?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) – Meu RH – A partir da release 12.1.34  
  
**Solução**

O objetivo desta documentação é auxiliar os nossos clientes na parametrização para aumentar o nível de segurança do Meu RH. Através de Pentest realizado internamente e pelos nossos clientes, chegamos em uma orientação que deve ser seguida para aumentar o nível de segurança do ambiente exposto na internet.

1. Habilitar o SSL:  
   Para garantir que a comunicação com o Meu RH seja segura, habilite o SSL para a sua aplicação no IIS. Isso é recomendado principalmente quando o portal é exposto em uma DMZ ou servidor com acesso via rede pública.

   Para isso é necessário adquirir um certificado através de uma autoridade certificadora confiável e seguir as documentações. Para mais informações acesse o link com exemplo de certificado SSL do Meu RH: [**RH - RM - Meu RH - Certificado HTTPS/SSL**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035159453-RH-RM-Meu-RH-Certificado-HTTPS-SSL?source=search)  
   **Importante:** Para que a mensagem de certificado inválido não seja exibida, o certificado deve ser adquirido por uma autoridade certificadora confiável e não um certificado Auto assinado do IIS.
2. Aplicar as configurações recomendadas de segurança para o portal Meu RH, conforme as orientações do link abaixo:  
   [**Recomendações de segurança Meu RH - Linha RM**](https://tdn.totvs.com/display/NPR/34.0+-+Linha+RM)  
     
   **Importante:** Todas as informações sugeridas acima foram checadas e testadas em um ambiente controlado com o apoio do nosso time de segurança e com resultados de Pentests executados internamente ou externamente pelos nossos clientes. No entanto, é recomendado que as configurações sejam realizadas inicialmente em um ambiente de homologação, devido à variedade e complexidade das configurações e especificidades dos servidores de cada cliente.
