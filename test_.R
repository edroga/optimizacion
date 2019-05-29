kkt_matrix<-(2*Sigma) %>% 
rbind(1) %>% 
rbind(r_i) %>% 
cbind(c(rep(1.0,ncol(Sigma)),0.0, 0.0)) %>% 
cbind(c(r_i, 0, 0))

b<-c(rep(0,ncol(Sigma)),1, rho)

solve(kkt_matrix, b, tol = 1e-7)
