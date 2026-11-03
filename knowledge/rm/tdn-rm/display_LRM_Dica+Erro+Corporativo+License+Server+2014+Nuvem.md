---
content_hash: 6765c40946fff3b2f66b64f344ac35f8aaddcd88a58da3c6179fca9374f23f6c
fetched_at: '2026-06-29T00:05:58.253040+00:00'
page_id: '185746558'
product: rm
source: tdn-rm
title: Dica Erro Corporativo License Server 2014 Nuvem
type: documentation
url: https://tdn.totvs.com/display/LRM/Dica+Erro+Corporativo+License+Server+2014+Nuvem
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework                       **Versão:**11.20 ou superior |
| **Processo** | **:** | License Server 2014 Nuvem |
| **Subprocesso** | **:** | Dica para correção de erro de CNPJ corporativo |
| **Data da publicação** | **:** | 20/03/2015 |

Em alguns ambientes é apresentado o erro de CNPJ corporativo ao validar a licença do license sever 2014 ( nuvem ).

Abaixo seguem algumas dicas para correção do erro.

**Erro: (-10008) - O** **License Server está rodando no modo corporativo, entretanto o CNPJ XX.XXX.XXX/XXXX-XX não está cadastrado para o uso de licenças corporativas**.

\_GoBack

1º - Verifique se a versão do Totvs License Server 2014 é a mais atual.

Para verificar a versão do License Server, acesse o Totvs License Server Monitor que esta disponivel no menu *Iniciar - Todos os programas - Totvslicense – Totvslicensemonitor* .   
 No Totvs License Sever Monitor ( Nuvem ) clique na opção de informação ( i ) localizado no canto superior direito. A versão do LS2014 deverá ser igual ou superior a 1.1.006 e a versão da Biblioteca RM também deverá estar atualizada.

2º - Acesse os Serviços do Windows e pare o serviço do License Server ( TOTVS | License Server ):

Após parar o serviço do License Server, realize o procedimento de exclusão do arquivo \_broker:

1.) Execute o RM.Host.ServiceManager no caminho C:\totvs\CorporeRM\RM.Net  
 2.) Pare o serviço   
 3.) Desinstale o serviço   
 4.) Exclua o arquivo \_broker.dat que se encontra na mesma pasta RM.Net   
 5.) Reinstale o serviço do host  
 6.) Inicialize o serviço do host

Feito isso, inicie novamente o serviço do Totvs License Server nos serviços do Windows e logo após logue novamente no sistema.

Se após estes procedimentos o erro ainda ocorrer, realize o procedimento abaixo:

Nos campos de **" ENDEREÇO** " e “**PORTA**”  preencha o IP e Porta do servidor de License Server corretamente e os confirmem de acordo com a instalação realizada. Após as verificações clique na opção ***SALVAR CONFIGURAÇÂO*** e após aparecer a mensagem “**CONFIGURAÇÕES SALVAS COM SUCESSO**” clique em **“OK”** e depois em ***CANCELAR***, não é necessário clicara no menu Realizar TESTE (este teste é destinado ao license com hardlock), clique em ok na mensagem de erro ate sair. Saia do sistema e entre novamente.

após aparecer a mensagem “**CONFIGURAÇÕES SALVAS COM SUCESSO**” clique em **“OK”**

clique em ok na mensagem de erro até sair. Saia do sistema e entre novamente.

Para maiores informações:

Consulte o [Wikihelp](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.LogAuditoria.aspx) TOTVS.

**COMUNIDADE** [@FRAMEWORK](https://totvs.byyou.com/?space=rframework)

**Canais de Atendimento:**

**Telefônico:** 4003-0015 escolhendo as opções 02 – dois (Software), 02 – dois (Suporte Técnico), 03 – três (RM), 09 – nove (Demais Áreas), 04 – quatro (BI) e 03 – três (Gerador de Relatórios e Planilha);

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)
