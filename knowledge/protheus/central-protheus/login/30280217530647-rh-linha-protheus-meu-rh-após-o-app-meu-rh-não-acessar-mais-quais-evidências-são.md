---
article_id: 30280217530647
category: LOGIN
content_hash: 69ea65d98c88baf00a0742faa0e941b68ccd6b3e17d74c65046abf93ce71af35
fetched_at: '2026-06-28T22:44:40.386842+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - Meu RH - Após o App Meu RH não acessar mais, quais evidências
  são necessárias para abrir um ticket ao Suporte
type: support-article
updated_at: '2026-06-23T21:25:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30280217530647-RH-Linha-Protheus-Meu-RH-Ap%C3%B3s-o-App-Meu-RH-n%C3%A3o-acessar-mais-quais-evid%C3%AAncias-s%C3%A3o-necess%C3%A1rias-para-abrir-um-ticket-ao-Suporte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30280203328919) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Após o App Meu RH não acessar mais, quais evidências são necessárias para abrir um ticket ao Suporte?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Por algum motivo, o App Meu RH pode sofrer alguma instabilidade, ou falha de configuração que resulte em i**ndisponibilidade do serviço.**  
  
Inicialmente, será necessário realizar as atualizações a seguir, pois estas precisam ser periodicamente executadas:  
  
- expedição contínua GPE (se possível rodar o *UPDDISTR*) para **atualização do RPO:** <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO>  
- **LIB** mais recente: <https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/>  
- **Arquivos de portal** na pasta Protheus\_data/web, conforme documentação:  <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034>   
**\*\*\*Dica de atualização:**  
Dentro do diretório atual, delete todos os arquivos existentes, menos o **properties.json**, assim a pasta terá somente os arquivos atualizados.  
  
Após as atualizações feitas, é necessário reiniciar os serviços e realizar os testes novamente, porém se mesmo assim não tiver sucesso, abra um *ticket* ao Suporte para continuidade, **com as evidências a seguir**, **após ter realizado as atualizações propostas:**  
  
- appserver.ini e properties.json utilizados  
- *QR Code* utilizado no celular  
- usuário e senha para testes de acesso  
- console.log do serviço após o erro ser gerado  
- extrato de versão Protheus com as datas dos fontes do RPO após atualizar  
- demais informações que nos auxiliem  
  
**Para clientes hospedados no *Cloud* na TOTVS**, poderá ser solicitada as atualizações diretamente à Equipe correspondente, sendo possível também **realizá-las via Ferramenta *T-Cloud*,** assim como a obtenção das evidências a serem enviadas ao Suporte.  
  
Para envio de informações sensíveis, como usuário e senha, recomenda-se a utilização da Ferramenta Minha Senha TOTVS: <https://minhasenha.totvs.com.br/home>  
  
**Saiba Mais:  
[RH - Linha Protheus - MEU RH - Como configurar o APPSERVER.INI, PROPERTIES.JSON e URL do QRCODE para acesso ao MEU RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044715514)**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
