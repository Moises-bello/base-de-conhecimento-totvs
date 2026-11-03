---
content_hash: 56462bdc221aa839e31aabebcdbc23850b525c6cfd8ffd0880929b3d1ec8c0c0
fetched_at: '2026-06-29T00:11:38.123734+00:00'
page_id: '781214336'
product: rm
source: tdn-rm
title: CERC - Teste Basico EndPoint
type: documentation
url: https://tdn.totvs.com/display/LRM/CERC+-+Teste+Basico+EndPoint
version: 3
---

Este documento tem como objetivo demonstrar o teste básico utilizando o powerShell no servidor onde tem a instalação do RM (TCGI), com proposito de validar se a segurança de rede do servidor está permitindo a comunicação com servidores extenos (Endpoints de sistemas terceiros).

**Copie e cole o script abaixo no powerShell:**

# Defina as credenciais de autenticação  
$username = "informe aqui ClientId"  
$password = "informe aqui ClientSecret"

# Codifique as credenciais em Base64  
$base64AuthInfo = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes("${username}:${password}"))

# Defina o endpoint da API  
$endpoint = "<https://ap-homolog.cerc.inf.br/oauth/token>"

# Defina o corpo da solicitação com grant\_type e value  
$body = @{  
    grant\_type = "client\_credentials"  
    value = "client\_credentials"

}

# Converta o corpo para form-data  
$formData = "grant\_type=client\_credentials&value=client\_credentials"

# Defina o cabeçalho Content-Type para form-data  
$headers = @{  
    "Authorization" = "Basic $base64AuthInfo"  
    "Content-Type" = "application/x-www-form-urlencoded"

}

# Faça a solicitação HTTP com autenticação básica e corpo form-data usando o Invoke-RestMethod  
$response = Invoke-RestMethod -Uri $endpoint -Method Post -Headers $headers -Body $formData

# Exiba a resposta  
$response

**FAQ:**

**Forbidden 403**  
O erro "403 Proibido" indica que o servidor recusou a solicitação devido à autenticação ou permissões insuficientes.   
Isso significa que a autenticação básica com as credenciais fornecidas não foi bem-sucedida.  
  
Existem algumas possíveis causas para esse problema:  
Credenciais incorretas: Verifique novamente as credenciais (username e password) para garantir que estejam corretas. Se necessário, obtenha novas credenciais válidas para autenticação.  
  
Bloqueio de IP ou Firewall: É possível que o servidor esteja bloqueando o IP da sua máquina ou que um firewall esteja impedindo o acesso à API. Verifique se há algum bloqueio de IP ou configuração de firewall que possa estar causando o erro.
