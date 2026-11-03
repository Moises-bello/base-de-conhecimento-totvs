---
content_hash: f28a4ca9036d586d6d0811b4f69a4fdb20960a8a4f7758103667940453e3d62d
fetched_at: '2026-06-29T00:08:53.477254+00:00'
page_id: '345541505'
product: rm
source: tdn-rm
title: 18 - Análise estatística via Google Analytics
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=345541505
version: 11
---

No novo portal do processo seletivo é possível configurar o serviço do Google Analytics.

Google Analytics é um serviço oferecido pela Google que expõe, entre outras coisas, estatísticas sobre o tráfego do site configurado.

Para realizar a configuração será necessário criar uma conta conforme o link abaixo: <https://analytics.google.com/analytics/web/>

A criação da conta é simples e basta seguir os três passos conforme abaixo.

No momento da criação da conta é importante informar algumas informações como:

**Nome do Proprietário –** Nome que será utilizado na criação da conta do Google Analytics onde serão controlado as informações do site.

**URL Padrão –** URL pública utilizada pelo novo Portal do Processo Seletivo.

**Ex:** [http://DOMINIO:PORTA/WEB/APP/EDU/PORTALPROCESSOSELETIVO](http://DOMINIOPORTA)

Finalizando o processo de criação da conta será gerado uma chave e também será exibido no Google Analytics uma instrução de código que deve ser informado no novo Portal do Processo Seletivo para iniciar o controle das informações.

**Obs:** O código acima 'UA-114421510-1' é único e deve ser utilizado o que foi gerado para a conta criada.  
Para iniciar o controle das informações do Google Analytics, basta copiar o código de acompanhamento gerado e colar no arquivo de ‘Index.html’ disponível no caminho padrão do instalador do novo Portal do Processo Seletivo. “C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\PortalProcessoSeletivo”.

Após os passos acima, o Google Analytics está pronto para começar a receber informações relativas ao Portal do Processo Seletivo.

**Importante:**

1. Para toda atualização de versão, o arquivo “Index.html” deve ser editado novamente para compor o código informado acima. Estamos trabalhando para que em futuras versões isso não seja necessário.
2. O Google Analytics não é uma ferramenta da TOTVS e não realizamos manutenção e atendimento em relação à essa ferramenta.

O **TOTVS Processo Seletivo** está preparado para registrar no Google Analytics apenas o carregamento inicial da aplicação, ou seja, a **URL principal**.

As mudanças de rota internas no portal do Processo Seletivo **não** disparam automaticamente novos eventos de visualização no Google Analytics. Isso significa que, por exemplo, ao confirmar uma inscrição ou emitir um comprovante, nenhum evento adicional é enviado ao Google Analytics.
