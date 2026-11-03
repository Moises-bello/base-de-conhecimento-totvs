---
article_id: 38584527544727
category: Framework (Linha Protheus)
content_hash: 82e8271024d177f70c2d7074367b4c251ebe06c3be6f6e7b16c00ac7e8b27d67
fetched_at: '2026-06-28T22:42:15.802599+00:00'
product: protheus
section_id: 360011673134
source: central-protheus
title: Framework - Framework (Linha Protheus) - Mensagem de uso de Libs divergentes
type: support-article
updated_at: '2026-02-23T20:03:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38584527544727-Framework-Framework-Linha-Protheus-Mensagem-de-uso-de-Libs-divergentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38584527538583) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual a causa da mensagem de **Lib** diferentes ao acessar o ambiente?

**Ambiente**  
Protheus - Lib - à partir da versão 12.1.2510

**Causa**  
A partir da versão 20260119 (Release 2510), o sistema só permite o acesso a um mesmo ambiente utilizando uma única versão de biblioteca (lib). Essa validação cria um bloqueio de versão (Lock) e verifica os acessos concorrentes para garantir a estabilidade e segurança do ERP, prevenindo falhas. Caso o sistema identifique que uma lib diferente está em uso, uma mensagem de aviso detalhando a divergência e a conexão será exibida.

Com essa nova validação, a aplicação de libs "a quente" (com o sistema em pleno funcionamento) não é mais possível.

Adicionalmente, a utilização da chave *specialkey* afeta o lock feito no ambiente. É recomendado o uso do controle de lock pelo DBAccess, pois o lock já se torna exclusivo por banco de dados, dispensando o uso da chave *specialkey* e evitando problemas com esta validação.

Caso seja identificado acessos com versões divergentes, será apresentado uma mensagem com o detalhamento desta divergência.

![](https://tdn.totvs.com/download/attachments/983818634/image-2025-11-5_11-37-19.png?version=1&modificationDate=1762353439457&api=v2)

**Solução**

Para garantir que a nova lib seja aplicada corretamente e evitar o bloqueio por versões divergentes, siga as instruções:

1. Realize a aplicação da nova lib em um ambiente dedicado ou de forma exclusiva (sem concorrência de acessos).
2. Após a aplicação da nova lib, reinicie **todos** os servidores do ambiente para garantir que a atualização seja reconhecida e não haja conflito com as versões antigas.
3. Certifique-se de que cada ambiente possua sua própria *specialkey* configurada, caso não esteja utilizando o controle de lock nativo pelo DBAccess.

**Aviso**   
  
A utilização da chave **specialkey** afeta o lock feito no ambiente, portanto é importante que cada ambiente possua sua própria specialkey configurada.

Utilizando o controle de lock pelo dbaccess o lock já é exclusivo por db, com isso a chave specialkey não é mais utilizada, o que evita problemas com essa validação.

**Saiba mais**  
  
[Mais informações](https://tdn.totvs.com.br/display/public/framework/SpecialKey)  
[Mais informações sobre o lock pelo dbaccess](https://tdn.totvs.com/pages/viewpage.action?pageId=949425872)  
[Bloqueio no uso de Libs distintas no mesmo ambiente](https://tdn.totvs.com/pages/releaseview.action?pageId=983818634)
