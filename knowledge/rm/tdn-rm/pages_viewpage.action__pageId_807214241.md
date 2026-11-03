---
content_hash: 562b6cc45bed64b4fc43e5a5e1eecf5fd4c3e9efd323a8be9e7a0b61b7786afe
fetched_at: '2026-06-29T00:11:43.475685+00:00'
page_id: '807214241'
product: rm
source: tdn-rm
title: PI - Testes - Ambiente Cliente/Restore
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=807214241
version: 5
---

IMPORTANTE

 Os Arquivos do PHP customizado, Word, Pdf e outros instaladores uteis ja se encontram no caminho:            
<https://drive.google.com/drive/u/0/folders/1DnFsCZd-WiHsgPv-RLP17kBpjX0qxhWV>

**Montando com restore**  
  
1 - configurar no restore a instalação dos arquivos "Portais RM XXXXXX - XXX" de acordo com a versão desejada. Ao configurar selecione o caminho dentro de cada versão, sugestão "C:\RM\Atual\Release\Bin\wwwroot"  
2 - configurar no restore a instalação do FrameHtml para baixar, o PI virá dentro da pasta em "C:\RM\Atual\Release\FrameHTML\ **web** \app\Imb\PVI"  
3 - agora iremos mapear no IIS o PI (PVI) para ser acessado via url.  
4 - Abra o IIS, na arvore de conexões clique no nome da maquina, em Sites com o botão direito e crie um site com o nome desejado que ficar vinculado a versão que está criando o PI.  
  
Exemplo: PI\_1212205.  
no campo "Caminho físico" selecione a pasta que acabou de dar get pelo restore.  
Exemplo: "C:\RM\Atual\Release\FrameHTML\web\app\Imb\PVI"  
Escolha a porta que deseja utilizar.  
Exemplo: 8005

No IIS informa usuário especifico para login:

**Atenção:** Mudar para usuários na máquina local, procurar o usuário "IIS\_IUSRS" e dar permissão controle total para o mesmo e todos os outros.  
  
**Ambiente novo, não aparece para instalar e referenciar banco de dados.**  
  
**Solução:** Verificar se o php existe no diretório de acordo com o arquivo php.ini da pasta, geralmente fica em: C:\PHP7.3.24
