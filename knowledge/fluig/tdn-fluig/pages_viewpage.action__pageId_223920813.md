---
content_hash: 0ec87958ceaff4e6546a106e41fafac995580e5aa1b6496217c8a0af06e50101
fetched_at: '2026-06-28T21:35:19.807623+00:00'
page_id: '223920813'
product: fluig
source: tdn-fluig
title: ARQ - Mensagem "Houve uma falha na validação da licença" ou "Servidor LS não
  encontrado" ao acessar a plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223920813
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Ao acessar a plataforma ocorre o erro "Não foi possível verificar o licenciamento do Fluig! Servidor LS não encontrado." ou "Houve uma falha na validação da licença"?

**Figura 1 - Mensagem de "Servidor LS não encontrado na versão 1.6.1 e superiores**

**Figura 2 - Mensagem "Houve uma falha na validação da licença" na tela de login na versão 1.6 ou anterior**

# Causa

Este erro pode ser causado por uma falha na comunicação entre a plataforma e o servidor de licenças.

# Solução

Verifique se o endereço e a porta de conexão com o servidor de licenças está configurado corretamente, conforme descrito em .

Confira também se o serviço do License Server está iniciado. Se não estiver, será necessários iniciá-lo e posteriormente iniciar os serviços da plataforma novamente.

Se por algum motivo o servidor de licença estiver indisponível, você pode escolher clicar em  como medida de contingência a partir da atualização 1.6.1.

Na atualização 1.6 ou anteriores consulte a documentação
