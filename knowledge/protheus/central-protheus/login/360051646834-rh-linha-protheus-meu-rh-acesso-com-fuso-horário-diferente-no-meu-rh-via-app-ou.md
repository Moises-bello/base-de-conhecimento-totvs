---
article_id: 360051646834
category: LOGIN
content_hash: ae26d541059c44dcc74e1b6ff09fcba3aae1447d33c1dac85103fe7aa3dcf872
fetched_at: '2026-06-28T22:44:40.629758+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Acesso com fuso horário diferente no MEU RH
  via APP ou BROWSER
type: support-article
updated_at: '2026-06-19T17:10:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051646834-RH-Linha-Protheus-MEU-RH-Acesso-com-fuso-hor%C3%A1rio-diferente-no-MEU-RH-via-APP-ou-BROWSER
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24764071028759) Tempo aproximado para leitura: 00:06:00 min**  
**Dúvida**  
Acesso com fuso horário diferente no MEU RH via APP ou BROWSER  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**O MEU RH disponibiliza o fuso horário a partir das informações contidas nos arquivos de portais, portanto, faça a atualização dos arquivos de seu ambiente conforme o link abaixo:  
[**Como Atualizar os arquivos do Portal Meu RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
  
Após a atualização, verifique se o horário será corrigido. Caso continue com a diferença de fuso horário, configure o parâmetro **MV\_HVERAO**. Este parâmetro é responsável pela disponibilização do horário que o servidor disponibilizará para a aplicação do MEU RH.  
  
Para acessar este parâmetro é necessário seguir o caminho no configurador (**SIGACFG**) .  
**Base de dados -> Dicionário -> Bases de Dados.**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24768067778583)**Após:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24768412279063)  
  
**Parâmetro**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24768082885527)  
  
Atualmente o Meu RH captura o ***horário do servidor, somado à timezone atribuída à localização*** **(quando a geolocalização está habilitada)** do local em que a marcação ocorreu.  
  
**Quando não é utilizado a geolocalização, a marcação deve seguir com o horário do servidor, independentemente do horário registrado na máquina local em que a marcação foi efetuada.**Essas informações são o que o produto deve atender e estão mais detalhadas no link abaixo, mais especificamente na seção **Requisitos Técnicos no artigo a seguir**:  
<https://tdn.totvs.com/pages/viewpage.action?pageId=334338837>  
  
**IMPORTANTE:**Para tratamento correto quanto ao fuso horário, o Meu RH precisa estar em HTTPS - Protocolo seguro e com a Geolocalização ativada, senão por questões técnicas de implementação da Ferramenta, não conseguirão tratar essa questão.  
  
Segue artigo, de como habilitar o HTTPS, com o protocolo SSL, medicante **certificado contratado e de responsabilidade da Empresa.**  
[RH - Linha Protheus - MEU RH - Como configurar o SSL/HTTPS para acesso externo ao MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042649133-RH-Linha-Protheus-MEU-RH-Como-configurar-o-SSL-HTTPS-para-acesso-externo-ao-MEU-RH)  
  
***Segue como o Meu RH trata a questão do fuso horário:*****Tratamento Fuso Horário**É considerada a hora do servidor para o registro da marcação, mesmo que o usuário altere data e hora de seu *smartphone*.  
  
Também é considerado o fuso horário das localidades onde a marcação é registrada, convertendo a hora do servidor na hora do local da marcação.  
  
**Exemplos:**Empresa possui o servidor em São Paulo e possui funcionários nas cidades de São Paulo, Manaus e Lisboa:  
 ***Exemplo 1***

* Funcionário em São Paulo, registra o ponto as 08:00 (*hora do smartphone alterada para 08:00)*.
* Fuso Horário = 0 hora
* Hora Servidor = 09:00
* Marcação é gravada com o horário servidor + fuso, 09:00 + 00:00 = **09:00**

***Exemplo 2***

* Funcionário em Manaus, registra o ponto as 08:00 (horário local)
* Fuso Horário = -1 hora
* Hora Servidor = 09:00
* Marcação é gravada com o horário servidor + fuso, 09:00 - 01:00 = **08:00**

***Exemplo 3***

* Funcionário em Lisboa, registra o ponto as 08:00 (horário local considerando o fuso horário +3)
* Fuso Horário = +3 horas
* Hora Servidor = 05:00
* Marcação é gravada com o horário servidor + fuso, 05:00 + 03:00 = **08:00**

**Hoje no Meu RH é obrigatório que habilite a geolocalização no smartphone ou no browser para buscar a latitude e longitude, com estas informações será possível realizar o cálculo do fuso horário baseado na localização que foi realizada a marcação de ponto.**Por exemplo, temos o servidor do Meu RH alocado na cidade de São Paulo (GMT -3), com o horário atual de 14:00.Existe um colaborador que está trabalhando na cidade de Cuiabá - MS (GMT -4) e ao marcar o ponto com a localização habilitada será passada para o servidor o fuso horário de Cuiabá , as horas serão calculadas da seguinte forma:  
  
Busca o horário do servidor baseado no GMT 0 = 17:00 horas  
Aplica o fuso horário enviado pela localização GMT -4 = 13:00 horas  
Fuso horário sem a localização GMT -3 = 14:00   
  
**(Importante, se o funcionário desabilitar a geolocalização e marcar o ponto,** **será considerado o horário do servidor onde está locado, neste exemplo, SP (GMT-3)****Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
