---
article_id: 360052412773
category: LOGIN
content_hash: 30cf0ff0e131011f88a625e75dea6e13532d8148f1abc0d8ca1abb6afe3bd8a2
fetched_at: '2026-06-28T22:44:40.623050+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus -  MEU RH - Envio do "esqueceu a senha" quando se utiliza
  SSL/certificado digital
type: support-article
updated_at: '2026-06-19T17:01:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052412773-RH-Linha-Protheus-MEU-RH-Envio-do-esqueceu-a-senha-quando-se-utiliza-SSL-certificado-digital
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17998027178263) Tempo aproximado para leitura: 00:02:00 min****Ocorrência**Após a configuração do certificado digital (SSL), a opção "Esqueceu a senha" não envia o *e-mail*  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Causa**Este problema ocorre por decorrência da configuração incorreta da chave **PUBLIC** contida dentro do arquivo appserver.ini.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o arquivo **appserver.ini;**  
2. Localize a **TAG "[HTTPENV]";**  
3. Em seguida, atualize\altere a chave **PUBLIC** conforme abaixo  
  
**Public=fwjwt/refresh\_token,auth,setting/companySettings****ATENÇÃO:** Certifique-se sempre de estar com seu ambiente atualizado, pois são disponibilizadas periodicamente, atualizações com melhorias e correções no MEU RH. **[Como Atualizar os arquivos do Portal Meu RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
[Pacote de acumulado do RH no Portal de Cliente](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/Rh_expedicao)  
  
Saiba Mais:  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
