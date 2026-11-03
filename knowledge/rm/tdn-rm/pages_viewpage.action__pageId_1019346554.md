---
content_hash: 485fb9df09452d608f53a53c9e59d68cd81f2c6db150bdc29c7a705d9fa0c241
fetched_at: '2026-06-29T00:05:47.906337+00:00'
page_id: '1019346554'
product: rm
source: tdn-rm
title: Integração - RDStation - PI - Roleta de corretores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1019346554
version: 10
---

baixar o ngrok para disponibilizar porta do host publica, rd precisara acessar o webhook do PI através do Ngrok.  
<https://ngrok.com/downloads/windows>

- criar conta no ngrok - com email da totvs mesmo  
- depois deverá pegar o token da sua conta  
- abra o prompt do ngrok e cole o comando 'ngrok config add-authtoken 2vRiVPu5LI0Al61IJpoGgJ1UEa3\_7RwTu5gz2QP4L8K1ZHjso', onde ( 2vRiVPu5LI0Al61IJpoGgJ1UEa3\_7RwTu5gz2QP4L8K1ZHjso) será a chave da sua conta do ngrok  
- depois digite o comando 'ngrok http <http://localhost:8000>' para criar o tunel do webhook com PI do IIS, o valor de (<http://localhost:8000>) deve ser o caminho do seu PI no IIS

- AGORA PRECISAMOS CRIAR A INTEGRAÇÃO NO RDSTATION  
Logar no RDstation   
<https://accounts.rdstation.com.br/>  
[igor.melo@totvs.com.br](mailto:igor.melo@totvs.com.br)  
Totvs@123

RD Marketing - criando o aplicativo e chave para configurar no PI (<https://developers.rdstation.com/reference/criar-aplicativo-appstore#:~:text=RD%20Station%20ecosystem-,Creating%20your%20app,-Access%20the%20App>)  
- Também utilizamos a pratica de callback então veja o trecho de (callback URL)

RD CRM dentro do portal do RDStation - vá em Perfil, clicando no nome do usuário logado, assim terá visão do token da instancia  
65fdfe2a343ccc000d085af3

Nome do usuario logado > Integrações > WebHooks (Criar WebHook - Usar Gatilho - Oportunidade )  
Adicionando o webHook com o caminho criado no Ngrok e o final do webhook com o padrão do rdstation no RD Marketing  
<https://dcd1-177-55-224-193.ngrok-free.app> (Caminho criado pelo ngrok - pegar dentro do menu <<https://dashboard.ngrok.com/endpoints>> e deixar o terminal do ngrock instalado rodando na maquina)  
+  
/api/webhook/rdstation/ (Caminho fixo do RDStation colocado nos parametros do RM)  
+  
totvs (senha criada dentro do PI no menu RDStation <Integracao-RDStation-Aplicativos "RD Station - Token WebHook - Cadastro de Leads enviados pelo RD">)

Importante

Depois que estiver com tudo configurado e desejar verificar o que o RDStation tem entregado para o webhook no PI.  
você poderá utilizar o parâmetro: **imprimir\_log\_rdstation**  
ele não está em scripts no sistema para ser criado, pode criar o mesmo no cliente com o script abaixo, assim que criar e o valor for 1,  
irá imprimir os valores de dados que o RDStation entregou para o webhook, será impresso na pasta tmp com o inicio RDSTATION\_:  
  
INSERT INTO XPIPARAMETRO (ID, GRUPO, TITULO, VALOR\_PADRAO, VALOR, TIPO, VARIAVEL)  
SELECT   
    MAX(p.ID) + 1,  
    3,  
    'Imprimi os valores de dados que o RDStation entregou para o webhook, será impresso na pasta tmp com o inicio RDSTATION\_',  
    '1',  
    '1',  
    'log',  
    'imprimir\_log\_rdstation'  
FROM XPIPARAMETRO p
