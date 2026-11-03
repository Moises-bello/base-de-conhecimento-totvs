---
article_id: 360028388792
category: License Sever Virtual
content_hash: 1870709438619202a98510d5977eef9f0a9cb93b9ca8ea8b9b697c76706332a0
fetched_at: '2026-06-28T22:42:20.075150+00:00'
product: protheus
section_id: 360000075428
source: central-protheus
title: Framework - Linha Protheus - Perda da validade do TOTVS ID
type: support-article
updated_at: '2026-01-27T17:24:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028388792-Framework-Linha-Protheus-Perda-da-validade-do-TOTVS-ID
---

**Dúvida**  
Existem ocasiões que podem fazer com que o TOTVS ID seja invalidado, levando a parada do License Server?  
  
**Ambiente**  
Protheus - LS Virtual - Todas as versões  
  
**Solução**  
Sim, existem. A geração do **Código de Instalação** do License Server Virtual é feita baseado em 3 pontos: **SMBIOS**, **Porta do License Server** (no arquivo appserver.ini do LS) e **MAC Address** da Placa de Rede. Se algum destes pontos sofrer alteração no servidor onde o LS Virtual está instalado, o TOTVS ID será invalidado, fazendo com que as licenças parem de funcionar.  
  
Neste caso, é necessário gerar um novo TOTVS ID no Portal do Cliente / Gestão de Licenças, e utilizá-lo no Wizard de Instalação que irá se abrir ao tentar iniciar o Monitor de Licenças, como se fosse uma instalação nova.  
  
Maiores informações sobre esta configuração no link:  
<http://tdn.totvs.com/display/framework/Troubleshooting>  
  
**Virtualização e invalidação do TOTVS ID**  
A Virtual Machine deve ser configurada de modo que não permita duplicação do número serial BIOS UUID, duplicação do MAC Address dos adaptadores de Rede ou que numa operação de Move da Virtual Machine estas informações sejam alteradas. Caso isto aconteça o serviço de licenciamento irá ser interrompido sem aviso prévio.  
  
**Importante**  
Alguns HyperVisor, por padrão, alteram as informação de BIOS UUID a cada inicialização da Virtual Machine. Verifique com o fornecedor como fazer para fixar o valor.  
  
Quando efetuar qualquer manutenção na Virtual Machine, tenha certeza que nenhum placa de rede foi removida e que a porta do License Server não foi alterada, caso isto aconteça o serviço de licenciamento irá ser interrompido.  
  
Quando ocorre a invalidação do TOTVS ID, no primeiro acesso ao Monitor de Licenças, será exibida a seguinte janela, avisando da invalidação do TOTVS ID:  
![lsv_totvsid.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029117851)  
  
Ao Avançar, será exibida a tela do Wizard solicitando o novo TOTVS ID, que deve ser gerado no Portal do Cliente / Gestão de Licenças.
